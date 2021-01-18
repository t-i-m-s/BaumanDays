"""BaumanDays URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from BaumanDays import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainPage, name='MainPage'),
    path('login/', views.BaumandaysLoginView.as_view(), name='LogIn'),
    path('registration/', views.BaumandaysRegisterView.as_view(), name='Register'),
    path('logout/', views.BaumandaysLogoutView.as_view(), name='LogOut'),
    path('teacher_rating/', include('TeacherRating.urls'), name='TeacherRating'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
