from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
import html

def HomePage(request):
    return HttpResponseRedirect(reverse('menu:mainmenu'))