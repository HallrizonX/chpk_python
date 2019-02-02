from django.urls import path
from authorization.views import AuthIndex, RegisterIndex, LogoutHandler

urlpatterns = [
    path("login/", AuthIndex.as_view(), name="auth_login"),
    path("register/", RegisterIndex.as_view(), name="auth_register"),
    path("logout/", LogoutHandler.as_view(), name="auth_logout")
    #path("", SubjectIndex.as_view(), name="index"),
    #path("<str:slug>/", SubjectDetail.as_view(), name="detail_url"),
    #path("tags/<str:slug>/", TagDetail.as_view(), name="tags"),
    #path("<str:slug>/", PostDetail.as_view(), name="detail_url")
]
