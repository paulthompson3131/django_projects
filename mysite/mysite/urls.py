"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
    path('', TemplateView.as_view(template_name='menu/main-menu.html')),
    path("", include("menu.urls")),
"""

import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import RedirectView
from . import views

# Up two folders to serve "site" content
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path("",  views.HomePage, name="sitehome"),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path("hello/", include("hello.urls")),
    path("menu/", include("menu.urls")),
    path("session/", include("session.urls")),
    path("form/", include("form.urls")),
    path("getpost/", include("getpost.urls")),
    re_path(r'^site/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    ),
]
