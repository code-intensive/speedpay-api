import sys
from os import getenv
from pathlib import Path

from dotenv import load_dotenv

from speedpay.config.settings.corsheaders import *
from speedpay.config.settings.databases import *
from speedpay.config.settings.rest_framework import *
from speedpay.config.settings.simplejwt import *
from speedpay.config.settings.spectacular import *

load_dotenv()

# Build paths inside the project like this: PROJECT_ROOT / 'subdir'.
PROJECT_ROOT = Path(__file__).parent.parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

APPS_DIR = PROJECT_ROOT.joinpath("speedpay")

if APPS_DIR not in sys.path:
    sys.path.insert(0, APPS_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")
API_VERSION = "v1"
BASE_API_ENDPOINT = f"api/{API_VERSION}"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("DEBUG", False)

# Since allowed hosts should hold a list of hosts, the list comprehension
# helps to handle that, defaulting to an empty list if env key is missing
ALLOWED_HOSTS = getenv("API_HOST", "").split(",")

# Application definition
CORE_APPS = [
    "django.forms",
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.contenttypes",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "debug_toolbar",
    "rest_framework",
    "drf_spectacular",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
]

LOCAL_APPS = [
    "speedpay.authentication",
    "speedpay.users",
    "speedpay.wallets",
]

INSTALLED_APPS = CORE_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

MIDDLEWARE.insert(0, CORS_MIDDLEWARE)

if DEBUG:
    MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")

ROOT_URLCONF = "speedpay.config.routes.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_ROOT.joinpath("templates").resolve().as_posix()],
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "speedpay.config.gateways.wsgi.application"

ADMIN_EMAIL = "admin@speedpay.ng"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [PROJECT_ROOT.joinpath("locale").resolve().as_posix()]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = getenv(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.console.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "speedpay/admin/"

# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("code-intensive", "justtega97@gmail.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# CORS_URLS_REGEX = r'^/api/.*$'
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000/",
    "http://127.0.0.1:3000/",
]

DJANGO_SETTINGS_MODULE = getenv("DJANGO_SETTINGS_MODULE", "config.settings.settings")
# ------------------------------------------------------------------------------

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = PROJECT_ROOT.joinpath("staticfiles").resolve().as_posix()
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [PROJECT_ROOT.joinpath("static").resolve().as_posix()]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
# MEDIA_ROOT = PROJECT_ROOT.joinpath('media').resolve().as_posix()
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
# MEDIA_URL = '/media/'


# AUTHENTICATION
# ------------------------------------------------------------------------------

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.SpeedPayUser"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = f"/api/{API_VERSION}/docs/"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "/auth-view/login/"
