from django.urls import path
from rest_framework_simplejwt import views as simple_jwt_views

app_name = "auth"

urlpatterns = [
    path("login/", simple_jwt_views.token_obtain_pair, name="auth-login"),
    path("logout/", simple_jwt_views.token_blacklist, name="auth-logout"),
    path("refresh-token/", simple_jwt_views.token_refresh, name="auth-token-refresh"),
]
