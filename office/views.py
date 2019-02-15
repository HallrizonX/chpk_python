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
            return render(request, 'office/student/index.html', context=self.get_context_by_profile(user))
        elif user.access_profile == "teacher":
            return render(request, 'office/teacher/index.html', context=self.get_context_by_profile(user))

    def get_context_by_profile(self, user):
        if user.access_profile == "student":
            # context for student
            return {"user": user}
        elif user.access_profile == "teacher":
            # context for teacher
            teacher = Teacher.objects.get(profile__user=user.user)
            return {
                "user": user,
                "subjects": teacher.subjects,
                "files": teacher.files.all().order_by('subject__group__number', 'subject__name')
            }
