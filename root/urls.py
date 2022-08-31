"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('base.urls')),
    path('', include('about.urls')),
    path('', include('contact.urls')),
    path('', include('blog.urls')),
    path('', include('service.urls')),
    path('', include('gallery.urls')),
    path('', include('resources.urls')),
    path('', include('projects.urls')),
    path('', include('career.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler403 = 'base.views.error_403'
handler500 = 'base.views.error_500'

handler404 = 'base.views.error_404'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)