from django.urls import path
from .views import OfficeIndex

urlpatterns = [
    path("", OfficeIndex.as_view(), name="office_index"),

    #path("", SubjectIndex.as_view(), name="index"),
    #path("<str:slug>/", SubjectDetail.as_view(), name="detail_url"),
    #path("tags/<str:slug>/", TagDetail.as_view(), name="tags"),
    #path("<str:slug>/", PostDetail.as_view(), name="detail_url")

]
