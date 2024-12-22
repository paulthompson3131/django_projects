from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Menu, MenuContent


class MainMenuView(generic.ListView):
    template_name = "menu/generic-menu.html"
    context_object_name = "menu"

    def get_queryset(self):
        return Menu.objects.get(name="main_menu")

class FirstView(MainMenuView):
    def get_queryset(self):
        return Menu.objects.get(name="first_menu")

class SecondView(MainMenuView):
    def get_queryset(self):
        return Menu.objects.get(name="second_menu")

class ThirdView(MainMenuView):
    def get_queryset(self):
        return Menu.objects.get(name="third_menu")

def DoSomething(request):
    template_name = "menu/dosomething.html"
    return render(request, template_name)
