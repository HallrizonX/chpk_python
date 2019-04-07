from django.urls import path
from .views import TeacherFilesRequest, TeacherFilesAddRequest, TeacherGetFilesAjax, TeacherGetFilesSecureAjax, FindSubjectAjax

urlpatterns = [
    path("teacher.files/", TeacherFilesRequest.as_view(), name="teacher.files"),
    path("teacher.files.add/", TeacherFilesAddRequest.as_view(), name="teacher.files.add"),
    path("teacher.get.files/", TeacherGetFilesAjax.as_view(), name="teacher.get.files"),
    path("teacher.get.files.secure/", TeacherGetFilesSecureAjax.as_view(), name="teacher.get.files.secure"),
    path("find.subject/", FindSubjectAjax.as_view(), name="find.subject"),
    #path("<str:slug>/", SubjectDetail.as_view(), name="detail_url"),
    #path("tags/<str:slug>/", TagDetail.as_view(), name="tags"),
    #path("<str:slug>/", PostDetail.as_view(), name="detail_url")

]
