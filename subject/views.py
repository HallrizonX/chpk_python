from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from office.models import Subject, Teacher, Files


class SubjectIndex(LoginRequiredMixin, View):
    """ Class for get html template of all subjects"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        subjects = get_list_or_404(Subject.objects.order_by('group__number', 'name'))
        return render(request, 'subject/index.html', context={
            "subjects": subjects,
        })


class SubjectDetail(LoginRequiredMixin, View):
    """ Class for get detail subject"""
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request, slug):

        subject = get_object_or_404(Subject, slug=slug)
        teacher = get_object_or_404(Teacher, subjects__slug=slug)
        try:
            files = Files.objects.filter(subject__slug=slug)
        except FileNotFoundError:
            pass

        return render(request, 'subject/detail.html', context={
            "subject": subject,
            "teacher": teacher,
            "files": files,
        })
