from django.shortcuts import render
from authorization.models import Profile
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class OfficeIndex(LoginRequiredMixin, View):
    login_url = '/auth/login/'
    redirect_field_name = ''

    def get(self, request):
        user = get_object_or_404(Profile, user=request.user)

        if user.access_profile == "student":
            return render(request, 'office/index_student.html', context={"user": user})
        elif user.access_profile == "teacher":
            return render(request, 'office/index_student.html', context={"user": user})

        return render(request, 'office/not_access.html', context={})














#class PostDetail(ObjectDetailMixin, View):
#    model = Post
#    template = 'timetable/detail_group.html'
#    queryType = "post"

#class TagDetail(ObjectDetailMixin, View):
#    model = Post
#    template = 'timetable/tags.html'
#    queryType = "tag"
