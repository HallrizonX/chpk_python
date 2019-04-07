from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login


class UserTools:

    @staticmethod
    def authenticate(request, username: str, password: str, template: str):
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/office/')
            else:
                # Non active account
                return redirect('/')
        else:
            return render(request, template, context={"msg": "Логін або пароль не вірні"})
