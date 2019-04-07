from django.urls import path
from .views import TeacherFiles, TeacherFileAdd, TeacherGetFiles, TeacherGetFilesSecure, SubjectsFind

urlpatterns = [
    path("teacher.files/", TeacherFiles.as_view(), name="teacher.files"),
    path("teacher.files.add/", TeacherFileAdd.as_view(), name="teacher.files.add"),
    path("teacher.get.files/", TeacherGetFiles.as_view(), name="teacher.get.files"),
    path("teacher.get.files.secure/", TeacherGetFilesSecure.as_view(), name="teacher.get.files.secure"),
    path("subjects/", SubjectsFind.as_view(), name="subject.find"),
]
