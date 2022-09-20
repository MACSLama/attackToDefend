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
from tkinter import N
from django.contrib import admin
from django.urls import path
from Game.views import main , team, tutorial, taskChoiceBlue,taskChoiceRed,blue1, blue2,task1, task2,task3,task4,task5,task6, task7,result, about , scoring, end
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name="about"),
    path('tutorial/',tutorial),
    path('scoring/', scoring, name="scoring"),
    path('', main, name="main"),
    path('team/',team, name="team"),
    path('taskChoiceBlue/', taskChoiceBlue, name="taskChoiceBlue"),
    path('taskChoiceRed/', taskChoiceRed, name="taskChoiceRed"),
    path('blue1/', blue1, name="blue1"),
    path('blue2/', blue2, name="blue2"),
    path('task1/', task1 , name="task1"),
    path('task2/', task2 , name="task2"),
    path('task3/', task3, name="task3"),
    path('task4/', task4, name="task4"),
    path('task5/', task5, name="task5"),
    path('task6/', task6, name="task6"),
    path('task7/', task7, name="task7"),
    path('result/', result, name="result"),
    path('end/', end, name="end"),
]
    
    