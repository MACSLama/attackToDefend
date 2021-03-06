"""myGame URL Configuration

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
from django.urls import path
from theGame.views import main , team, tutorial, blue, task1, task2,task3,task4,task5,task6, task7,result, about , scoring
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('scoring/', scoring),
    path('', main),
    path('team/',team),
    path('tutorial/',tutorial),
    path('team/blue/', blue),
    path('team/blue/task1/', task1),
    path('team/blue/task2/', task2),
    path('team/blue/task3/', task3),
    path('team/blue/task4/', task4),
    path('team/blue/task5/', task5),
    path('team/blue/task6/', task6),
    path('team/blue/task7/', task7),
    path('team/blue/result/', result),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
