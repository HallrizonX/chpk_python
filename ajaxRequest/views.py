from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from office.models import *
from django.views.decorators.csrf import csrf_protect


class TeacherFilesRequest(LoginRequiredMixin, View):
    """ Class for change and remove file in DB"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    """ Change data file in DB"""

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
        return HttpResponseRedirect('/office/?id=' + str(f.subject_id))

    """ Remove file from DB"""

    def get(self, request):
        f = Files.objects.get(id=request.GET['id'])
        sub_id = f.subject_id
        f.delete()

        return JsonResponse({'id': sub_id})


class TeacherFilesAddRequest(LoginRequiredMixin, View):
    """ Class for adding new file in DB"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def post(self, request):
        subject = Subject.objects.get(id=request.POST["subject"])

        f = Files(file=request.FILES["file"], title=request.POST["title"], subject_id=subject.id)
        f.save()
        teacher = Teacher.objects.get(profile__user=request.user)
        teacher.files.add(f)
        teacher.save()
        return HttpResponseRedirect('/office/')


class TeacherGetFilesAjax(LoginRequiredMixin, View):
    """ Class for get html template with data of files by ajax request and ID certain subject"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        files = Files.objects.all().filter(subject_id=request.GET["id"])

        return render(request, 'office/teacher/print-files.html', context={'files': files})
