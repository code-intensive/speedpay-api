from decimal import Decimal
from typing import Any, Tuple

from django.contrib.auth import get_user_model
from django.db import models, transaction
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError

from speedpay.utils.id_generator import generate_uuid

SpeedPayUser = get_user_model()


class SpeedPayWallet(models.Model):
    """SpeedPay Wallet Model"""

    MAX_BALANCE = Decimal(9_999_999.00)
    speedpay_user = models.ForeignKey(
        SpeedPayUser,
        verbose_name=_("speedpay user"),
        db_index=True,
        on_delete=models.CASCADE,
        related_name="wallets",
    )
    balance = models.DecimalField(
        help_text=_("The current available money in the wallet"),
        db_index=True,
        max_digits=9,
        decimal_places=2,
        default=0,
    )
    wallet_uuid = models.CharField(
        _("wallet uuid"),
        default=generate_uuid("wallet"),
        db_index=True,
        max_length=80,
        help_text=_("A universally unique identifier for this wallet"),
    )
    last_withdrawn = models.DateTimeField(
        help_text=_("Last time a withdrawal was made from this wallet"),
        null=True,
    )
    last_deposited = models.DateTimeField(
        help_text=_("Last time a deposit was made to this wallet"),
        null=True,
    )
    is_active = models.BooleanField(
        help_text=_("For implementing wallet disabling"),
        default=True,
    )

    @property
    def is_empty(self) -> bool:
        """Check if the current balace is greater than zero"""
        return Decimal(self.balance) < Decimal(1)

    def withdraw(self, amount: Any) -> models.Model:
        """Withdraws specified amount from this wallet"""
        can_withdraw, new_balance = self.inspect_withdrawal(amount)
        if not can_withdraw:
            raise ValidationError(
                detail=(
                    f"You currently cannot withdraw {amount} due to insufficient funds"
                ),
                code="insufficient_funds",
            )
        with transaction.atomic():
            self.balance = new_balance
            self.last_withdrawn = timezone.now()
            self.save(update_fields=["balance", "last_withdrawn"])
        self.refresh_from_db(fields=["balance", "last_withdrawn"])

    def deposit(self, amount: Any) -> models.Model:
        """Deposits specified amount from this wallet"""
        can_deposit, new_balance = self.inspect_deposit(amount)
        if not can_deposit:
            raise ValidationError(
                detail=(f"{amount} exceeds the maximum funds of {self.MAX_BALANCE}"),
                code="excess_deposit",
            )
        with transaction.atomic():
            self.balance = new_balance
            self.last_deposited = timezone.now()
            self.save(update_fields=["balance", "last_deposited"])
        self.refresh_from_db(fields=["balance", "last_deposited"])

    def inspect_withdrawal(self, amount: Any) -> Tuple[bool, Decimal]:
        """Validates if the current withdrawal transaction is possible"""
        balance_remaining = SpeedPayWallet._mock_withdrawal(self.balance, amount)
        is_withdrawable = (not self.is_empty) and (balance_remaining >= Decimal(0))
        return (is_withdrawable, balance_remaining)

    def inspect_deposit(self, amount: Any) -> Tuple[bool, Decimal]:
        """Validates if the current deposit transaction is possible"""
        new_balance = SpeedPayWallet._mock_deposit(self.balance, amount)
        limit_not_exceeded = self.MAX_BALANCE > new_balance
        return limit_not_exceeded, new_balance

    @staticmethod
    def _mock_deposit(current_balance: Any, amount_requested: Any) -> Decimal:
        """Calculates the sum of `current_balance` and `requested_amount`"""
        return Decimal(current_balance) + Decimal(amount_requested)

    @staticmethod
    def _mock_withdrawal(current_balance: Any, amount_requested: Any) -> Decimal:
        """Calculates the difference between `current_balance` and `requested_amount`"""
        return Decimal(current_balance) - Decimal(amount_requested)
