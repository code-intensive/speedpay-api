__all__ = ("DATABASES",)


# from os import getenv

# from dotenv import load_dotenv


# load_dotenv()


# DATABASES = {

#     'default': {

#         'ENGINE': 'django.db.backends.postgresql_psycopg2',

#         'NAME': getenv('DB_NAME'),

#         'USER': getenv('DB_USER'),

#         'PASSWORD': getenv('DB_PASSWORD'),

#         'HOST': getenv('DB_HOST'),

#         'PORT': getenv('DB_PORT'),

#     }
# }


from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}
