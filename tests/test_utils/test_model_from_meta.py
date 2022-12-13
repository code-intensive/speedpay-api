from speedpay_users.api.serializers import SpeedPayUserSerializer
from speedpay_users.models import SpeedPayUser
from speedpay_wallet.api.serializers import SpeedPayWalletSerializer
from speedpay_wallet.models import SpeedPayWallet
from utils import model_from_meta


def test_model_from_meta():
    assert SpeedPayUser is model_from_meta(SpeedPayUserSerializer)


def test_model_from_metal_fails():
    assert SpeedPayWallet is not model_from_meta(SpeedPayWalletSerializer)


def test_model_from_meta_assertion():
    try:
        model_from_meta(SpeedPayUser)
    except AssertionError:
        pass
    else:
        raise AssertionError(
            "SpeedPayUser Model is not a valid ModelSerializer subclass",
        )
