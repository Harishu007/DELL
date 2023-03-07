"""dell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from laptop.views import *
from mobile.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_lap/',first_lap,name='first_lap'),
    path('second_lap/',second_lap,name='second_lap'),
    path('first_mobile/',first_mobile,name='first_mobile'),
    path('second_mobile/',second_mobile,name='second_mobile'),



]
