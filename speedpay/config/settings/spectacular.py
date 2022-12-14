__all__ = ("SPECTACULAR_SETTINGS",)


# By Default swagger ui is available only to admin user(s). You can change permission classes to change that
# See more configuration options at
# https://drf-spectacular.readthedocs.io/en/latest/settings.html#settings
SPECTACULAR_SETTINGS = {
    "TITLE": "SpeedPay API",
    "DESCRIPTION": "Open API automatic documentation for Speedpay's API endpoints",
    "VERSION": "1.0.0",
    "SERVE_PERMISSIONS": ["rest_framework.permissions.IsAuthenticated"],
    "SERVERS": [
        {"url": "http://127.0.0.1:8000", "description": "Local Development server"},
        # {'url': 'http://104.168.175.34:8000', 'description': 'Staging Development server'},
        # {'url': 'https://spirit_stream.gghnigeria.org', 'description': 'Production server'},
    ],
}
