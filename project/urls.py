"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic.base import TemplateView
<<<<<<< HEAD
from project.components.ratingList.RatingList import rating_list

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('accounts/', include('project.components.accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/rating-list/', rating_list, name='rating_list')
=======
from acounts import views


urlpatterns = [
    path('accounts/', include('acounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('questions/', views.get_all_questions,
         name="questions"),
    path('results/', views.get_results,
         name="results"),
    path('admin/', admin.site.urls),
>>>>>>> 3beede4cb98aa64b5d663c867d8e6c0eb7333fa1

]
