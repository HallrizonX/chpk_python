from django.shortcuts import render
from authorization.models import Profile
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from office.utils.OfficeFactory import OfficeFactory


class OfficeIndex(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        try:
            office = OfficeFactory.create(Profile.objects.get(user=request.user))
            return render(request, template_name=office.template, context=office.get_context())
        except:
            return render(request, 'office/not_access.html', {})
