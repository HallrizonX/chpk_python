from django.urls import path
from .views import TeacherDetail, TeacherIndex

urlpatterns = [
    path("", TeacherIndex.as_view(), name="teacher_index"),
    path("<str:username>/", TeacherDetail.as_view(), name="teacher_detail"),
]
