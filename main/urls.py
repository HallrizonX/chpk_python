from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect


def home(request):
    return redirect('/auth/login/')


urlpatterns = [
    path('admin/', admin.site.urls),
    # Home
    path('', home, name="home"),
    # Authorization and registration
    path('auth/', include('authorization.urls')),
    # Personal room for register users
    path('office/', include('office.urls')),
    # Subjects
    path('subject/', include('subject.urls')),
    # Teacher
    path('teacher/', include('teacher.urls')),
    # Ajax, Post, Get requests from form
    path('api/', include('api.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
