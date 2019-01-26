from django.urls import path
from .views import SubjectIndex, SubjectDetail

urlpatterns = [
    path("", SubjectIndex.as_view(), name="subject_index"),
    path("<str:slug>/", SubjectDetail.as_view(), name="subject_detail"),
]
