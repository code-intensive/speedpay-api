__all__ = ("DATABASES",)


from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


BASE_DIR = Path(__file__).parent.parent.parent

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    "pythonanywhere": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": getenv("DB_NAME"),
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "HOST": getenv("DB_HOST"),
        "PORT": getenv("DB_PORT"),
    },
}
