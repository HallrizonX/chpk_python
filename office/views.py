from django.shortcuts import render
from authorization.models import Profile
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class OfficeIndex(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        user = get_object_or_404(Profile, user=request.user)

        if user.access_profile == "student":
            return render(request, 'office/student/index_student.html', context={"user": user})
        elif user.access_profile == "teacher":

            teacher = Teacher.objects.get(profile__user=request.user)
            return render(request, 'office/teacher/index_teacher.html', context={
                "user": user,
                "subjects": teacher.subjects,
                "files": teacher.files.all().order_by('subject__group__number', 'subject__name')
            })

        return render(request, 'office/not_access.html', context={})
