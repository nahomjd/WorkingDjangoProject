"""db_webapp_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views
app_name = 'main'  # here for namespacing of urls.


urlpatterns = [
    path('', views.index, name="index"),
    path('database/', views.database, name="demo"),
    path('database2/', views.database2, name="demo"),
    path('database3/', views.database3, name="demo"),
    path('database4/', views.database4, name="demo"),
    path('database5/', views.database5, name="demo"),
    path('database6/', views.database6, name="demo"),
]
