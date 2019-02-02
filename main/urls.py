from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home
    path('', TemplateView.as_view(template_name='home/base.html'), name="home"),
    # Authorization and registration
    path('auth/', include('authorization.urls')),
    # Personal room for register users
    path('office/', include('office.urls')),
    # Subjects
    path('subject/', include('subject.urls')),
    # Ajax requests
    path('api/', include('ajaxRequest.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
