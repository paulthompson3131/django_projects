from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


def MainMenuView(request):
    template_name = "menu/main-menu.html"
    main_menu_list = [
         {"label": "This is menu Option 1", "url_to_call": "first_url" },
         {"label": "This is menu Option 2", "url_to_call": "second_url" },
         {"label": "This is menu Option 3", "url_to_call": "third_url" }
        ]
    context = { "main_menu_list": main_menu_list }
    return render(request, template_name, context)

def FirstView(request):
    template_name = "menu/first.html"
    first_command_list = [
         {"label": "Find out what people are doing", "url_to_call": "dosomething" },
         {"label": "Get Accounting Details", "url_to_call": "dosomething" },
         {"label": "Get Batch Execution Details", "url_to_call": "dosomething" }
        ]

    context = { "first_command_list":first_command_list }
    return render(request, template_name, context)

def SecondView(request):
    template_name = "menu/second.html"
    second_command_list = [
         {"label": "Find out how to Climb Trees", "url_to_call": "dosomething" },
         {"label": "Get Car Details", "url_to_call": "dosomething" },
         {"label": "Get Astronomical  Details", "url_to_call": "dosomething" }
        ]

    context = { "second_command_list":second_command_list }
    return render(request, template_name, context)

def ThirdView(request):
    template_name = "menu/third.html"
    third_command_list = [
         {"label": "Find out how to Watch Movies", "url_to_call": "dosomething" },
         {"label": "Get Bike Details", "url_to_call": "dosomething" },
         {"label": "Get Astronomical Cqalendars", "url_to_call": "dosomething" }
        ]

    context = { "third_command_list":third_command_list }
    return render(request, template_name, context)

def DoSomething(request):
    template_name = "menu/dosomething.html"
    dummy = "dummy"
    context = { "dummy": dummy }
    return render(request, template_name, context)
