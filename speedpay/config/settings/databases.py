__all__ = ("DATABASES",)


from os import getenv

from dotenv import load_dotenv

load_dotenv()


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": getenv("DB_NAME"),
        "USER": getenv("DB_USER"),
        "PASSWORD": getenv("DB_PASSWORD"),
        "HOST": getenv("DB_HOST"),
        "PORT": getenv("DB_PORT"),
    },
}
