# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from core import settings
from core.settings import STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landingpage.urls')),
    path('works/', include('works.urls')),
    path('blogs/', include('blog.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


