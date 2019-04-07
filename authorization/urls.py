from django.urls import path
from authorization.views import AuthIndex, RegisterIndex, LogoutHandler

urlpatterns = [
    path("login/", AuthIndex.as_view(), name="auth_login"),
    path("register/", RegisterIndex.as_view(), name="auth_register"),
    path("logout/", LogoutHandler.as_view(), name="auth_logout")
]
