from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView

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

class DoSomethingView(TemplateView):
    template_name = 'menu/dosomething.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "Do Something With Your Life"
        context['subheading'] = "Anything Other than Watching your devices or TV all Day"
        context['listofideas'] = ['Play ball with the children','Water the Tomatos', 'Ride a Bike']

        return context
