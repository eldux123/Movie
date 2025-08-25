"""
URL configuration for Peliculas project.
"""

from django.contrib import admin
from django.urls import path, include
from Peliculas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),      # Página principal
    path('about/', views.about, name='about'),  # Página "Acerca de"
    path('news/', include('news.urls')),    # App de noticias

    path('signup/', views.signup, name='signup'),

    path('statistics/', views.statistics, name='statistics'),

]

# Servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
