from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home/base.html'), name="home"),
    path('auth/', include('authorization.urls')),
    path('office/', include('office.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
