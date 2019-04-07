from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from authorization.utils.DBAudit import DBAudit
from authorization.utils.UserTools import UserTools



class AuthMixin:
    """ Class for process authorization users """
    template = ""


    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/office/')
        return render(request, self.template, context={})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/office/')
        return UserTools.authenticate(request,
                                      username=request.POST['username'],
                                      password=request.POST['password'],
                                      template=self.template)


class RegisterMixin:
    """ Class for process registration new users """
    model = None
    template = ""
    href = "/auth/register/"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/office/')
        return render(request, self.template, context={})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/office/')
        data = request.POST
        if not DBAudit.check_email(data['email']) or not DBAudit.check_username(data['username']):
            return render(request, self.template, context={"msg": "Помилка з логіном або поштою"})

        # Create user
        User.objects.create_user(username=str(data['username']),
                                 email=str(data['email']),
                                 password=str(data['password']))
        # Create profile
        if self.create_profile(data):
            return UserTools.authenticate(request,
                                          username=data['username'],
                                          password=data['password'],
                                          template=self.template)

        return render(request, self.template, context={"msg": "Помилка реєстрації"})

    def create_profile(self, data: dict) -> bool:
        try:
            profile = self.model.objects.get(user__username=str(data['username']))
            profile.name = str(data['name'])
            profile.surname = str(data['surname'])
            profile.last_name = str(data['last_name'])
            profile.save()
            return True
        except:
            return False


class LogoutMixin:
    """ Class for process logout users """
    href = ""

    def get(self, request):
        logout(request)
        return redirect(self.href)

    def post(self, request):
        logout(request)
        return redirect(self.href)
