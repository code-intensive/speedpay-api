from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from speedpay.utils.id_generator import generate_uuid


class SpeedPayUser(AbstractUser):
    is_active = models.BooleanField(_("active status"), default=True)
    email = models.EmailField(_("email address"), unique=True)
    is_admin = models.BooleanField(_("admin status"), default=False)
    uuid = models.CharField(
        _("user uuid"),
        default=generate_uuid("user"),
        db_index=True,
        max_length=80,
    )
