from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from office.models import *
from django.views.decorators.csrf import csrf_protect


class TeacherFilesRequest(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = ''


    def post(self, request):
        f = Files.objects.get(id=request.POST["id"])

        if request.POST["title"].replace(" ", "") != "":
            f.title = request.POST["title"]
        try:
            if request.FILES["file"] is not None and request.FILES["file"] != "":
                f.file = request.FILES["file"]
        except:
            pass

        f.save()

        return HttpResponseRedirect('/office/#href-'+str(f.id))


    def get(self, request):
        Files.objects.get(id=request.GET['id']).delete()

        return HttpResponse()


