from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # SWAGGER AND SPECTACULAR BROWSEABLE API VIEWS
    path(
        f"{settings.BASE_API_ENDPOINT}/schema/",
        SpectacularAPIView.as_view(),
        name="api-schema",
    ),
    path(
        f"{settings.BASE_API_ENDPOINT}/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    path(settings.ADMIN_URL, admin.site.urls),
    # Business layer API urls
    path("", include("config.routes.api_urls")),
    # Default auth views from rest framework for session based sign in
    path("auth-view/", include("rest_framework.urls")),
    # Simple JWT authentication endpoints
    path(
        f"{settings.BASE_API_ENDPOINT}/auth/",
        include("speedpay.authentication.urls"),
    ),
]


if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    #
    # Additionally, the debug toolbar and media routes are added during development.
    import debug_toolbar
    from django.views import defaults as default_views

    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
        path("__debug__/", include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
