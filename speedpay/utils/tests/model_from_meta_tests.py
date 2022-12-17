from speedpay.users.api.serializers import SpeedPayUserSerializer
from speedpay.users.models import SpeedPayUser
from speedpay.utils.model_extractor import model_from_meta
from speedpay.wallets.models import SpeedPayWallet


def test_model_from_meta():
    assert SpeedPayUser is model_from_meta(SpeedPayUserSerializer)


def test_model_from_metal_fails():
    assert SpeedPayWallet is not model_from_meta(SpeedPayUserSerializer)


def test_model_from_meta_assertion():
    try:
        model_from_meta(SpeedPayUser)
    except AssertionError:
        pass
    else:
        raise AssertionError(
            f"{type(SpeedPayUser)} Model is not a valid ModelSerializer subclass",
        )
