from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Add URL for new user registration here.
    path('register/', views.register, name='register'),
    path('', views.upload_view, name='upload'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
