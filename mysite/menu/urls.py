from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path("", views.MainMenuView, name="mainmenu"),
    path("first_url", views.FirstView, name="first_url"),
    path("second_url", views.SecondView, name="second_url"),
    path("third_url", views.ThirdView, name="third_url"),
    path("dosomething", views.DoSomething, name="dosomething"),
]
