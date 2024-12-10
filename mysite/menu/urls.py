from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'menu'

urlpatterns = [
    path("", views.mainmenu.as_view(), name="mainmenu"),
    path('menu11', views.menu11.as_view(), name='menu11'),
    path('menu12', views.menu12.as_view(), name='menu12'),
    path('menu13', views.menu13.as_view(), name='menu13'),
    path('peoplelist', views.peoplelist.as_view(), name='peoplelist'),
    path('getform', views.getform, name='getform'),
    path('postform', views.postform, name='postform'),

]
