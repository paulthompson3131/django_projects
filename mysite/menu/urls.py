from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path("", views.MainMenuView.as_view(), name="mainmenu"),
    path("first_url", views.FirstView.as_view(), name="first_url"),
    path("second_url", views.SecondView.as_view(), name="second_url"),
    path("third_url", views.ThirdView.as_view(), name="third_url"),
    path("dosomething", views.DoSomethingView.as_view(), name="dosomething"),
]
