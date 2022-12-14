__all__ = (
    "CORS_ALLOW_METHODS",
    "CORS_MIDDLEWARE",
    "CORS_ALLOW_ALL_ORIGINS",
    "CORS_ALLOW_CREDENTIALS",
)


CORS_ALLOW_METHODS = [
    "PATCH",
    "POST",
    "PUT",
    "DELETE",
    "GET",
    "OPTIONS",
]

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_MIDDLEWARE = "corsheaders.middleware.CorsMiddleware"
