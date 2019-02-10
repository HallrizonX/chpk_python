from django.urls import path
from .views import TeacherFilesRequest, TeacherFilesAddRequest, TeacherGetFilesAjax

urlpatterns = [
    path("teacher.files/", TeacherFilesRequest.as_view(), name="teacher.files"),
    path("teacher.files.add/", TeacherFilesAddRequest.as_view(), name="teacher.files.add"),
    path("teacher.get.files/", TeacherGetFilesAjax.as_view(), name="teacher.files.add"),

    #path("<str:slug>/", SubjectDetail.as_view(), name="detail_url"),
    #path("tags/<str:slug>/", TagDetail.as_view(), name="tags"),
    #path("<str:slug>/", PostDetail.as_view(), name="detail_url")

]
