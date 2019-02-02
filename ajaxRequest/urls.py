from django.urls import path
from .views import TeacherFilesRequest

urlpatterns = [
    path("teacher.files/", TeacherFilesRequest.as_view(), name="teacher.files"),


    #path("<str:slug>/", SubjectDetail.as_view(), name="detail_url"),
    #path("tags/<str:slug>/", TagDetail.as_view(), name="tags"),
    #path("<str:slug>/", PostDetail.as_view(), name="detail_url")

]
