from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.id_generator import generate_uuid

SpeedPayUser = get_user_model()


class SpeedPayWallet(models.Model):
    """SpeedPay Wallet Model"""

    speedpay_user = models.ForeignKey(
        SpeedPayUser,
        verbose_name=_("speedpay user"),
        db_index=True,
        on_delete=models.CASCADE,
        related_name="wallets",
    )
    balance = models.DecimalField(
        _("wallet balance"),
        db_index=True,
        max_digits=9,
        decimal_places=2,
        default=0,
    )
    wallet_uuid = models.CharField(
        _("user uuid"),
        default=generate_uuid("wallet"),
        db_index=True,
        max_length=80,
    )
    last_withdrawn = models.DateTimeField(_("time of last withdrawal"), null=True)
    last_deposited = models.DateTimeField(_("time of last deposit"), null=True)
    is_active = models.BooleanField(_("is active"), default=True)

    @property
    def is_empty(self) -> bool:
        """Check if the current balace is greater than zero"""
        return Decimal(self.balance) < Decimal(0)

    def validate_withdrawal(self, amount: int) -> bool:
        """Validates if the current withdrawal transaction is possible"""
        return True if self.balance > amount else False
