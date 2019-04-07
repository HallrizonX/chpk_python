from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from office.models import *
import os


class TeacherFiles(LoginRequiredMixin, View):
    """ Class for change and remove file in DB"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    # Change data of file in DB
    def post(self, request):
        f = Files.objects.get(id=request.POST["id"])

        if request.POST["title"].replace(" ", "") != "":
            f.title = request.POST["title"]

            f.save()
        try:
            if request.FILES["file"] is not None and request.FILES["file"] != "":
                f.file = request.FILES["file"]
        except:
            return HttpResponseRedirect('/office/')

        f.save()
        return HttpResponseRedirect('/office/?id=' + str(f.subject_id))

    # Remove file from DB
    def get(self, request):
        f = Files.objects.get(id=request.GET['id'])
        sub_id, file_path = f.subject_id, f.file.path
        f.delete()
        os.remove(file_path)
        return JsonResponse({'id': sub_id})

class TeacherFileAdd(LoginRequiredMixin, View):
    """ Class for adding new file in DB"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def post(self, request):
        # writing data of file into DB (Files) and save local in folder /media/
        subject = Subject.objects.get(id=request.POST["subject"])
        f = Files(file=request.FILES["file"], title=request.POST["title"], subject_id=subject.id)
        f.save()
        # create relations between tables(File, Teacher)
        teacher = Teacher.objects.get(profile__user=request.user)
        teacher.files.add(f)
        teacher.save()

        return HttpResponseRedirect('/office/')

class TeacherGetFiles(LoginRequiredMixin, View):
    """ Class for get html template with data of files by ajax request and ID certain subject"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        files = Files.objects.all().filter(subject_id=request.GET["id"])

        return render(request, 'office/teacher/ajax-print-files.html', context={'files': files})

class TeacherGetFilesSecure(LoginRequiredMixin, View):
    """ Class for get html template with data of files by ajax request and ID certain subject"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        files = Files.objects.all().filter(subject_id=request.GET["id"])

        return render(request, 'office/teacher/ajax-print-files-secure.html', context={'files': files})

class SubjectsFind(LoginRequiredMixin, View):
    """ Class for get html template with data of files by ajax request and ID certain subject"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        if request.GET["text"] == "":
            subjects = Subject.objects.all().order_by()
        else:
            subjects = Subject.objects.filter(group__number__contains=request.GET["text"]).order_by('group__number')

        return render(request, 'subject/table.html', context={'subjects': subjects})
