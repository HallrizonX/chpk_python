from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from office.models import *


class SubjectIndex(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        subjects = get_list_or_404(Subject)
        return render(request, 'subject/index.html', context={
            "subjects": subjects,
        })


class SubjectDetail(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request, slug):

        subject = Subject.objects.get(slug=slug)
        teacher = Teacher.objects.get(subjects__slug=slug)
        files = Files.objects.all().filter(subject__slug=slug)
        return render(request, 'subject/detail.html', context={
            "subject": subject,
            "teacher": teacher,
            "files": files,
        })
