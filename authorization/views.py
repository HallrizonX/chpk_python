from django.views.generic import View
from authorization.models import Profile
from authorization.mixins import RegisterMixin, AuthMixin, LogoutMixin


class AuthIndex(AuthMixin, View):
    template = 'authorization/login.html'


class RegisterIndex(RegisterMixin, View):
    model = Profile
    template = "authorization/register.html"


class LogoutHandler(LogoutMixin, View):
    href = "/"
