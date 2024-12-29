from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView

from .models import Menu, MenuContent

from django.db import connections



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
    sql = "SELECT name, owner, birth from cats"
    sourcedb = "systemsupport"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = "The Cat List"
        context['subheading'] = "Cats and their Owners"
        with connections[self.sourcedb].cursor() as cursor:
            cursor.execute(self.sql)
            columns = [col[0] for col in cursor.description]
            context['rows'] = [dict(zip(columns, row)) for row in cursor.fetchall()]
            context['columns'] = []
            for key, val in context['rows'][0].items():
                context['columns'].append(key) 
        return context


class GetEmployeesView(DoSomethingView):
    sourcedb = "employees"
    sql = "SELECT emp_no,birth_date,first_name,last_name ,gender,hire_date from employees where last_name like 'Tho%' and hire_date > '1996-10-10' order by last_name"

class GetEmployeesDepartmentView(DoSomethingView):
    sourcedb = "employees"
    sql = "select e.first_name, e.last_name, e.emp_no, d.dept_name from dept_emp de inner join employees e on de.emp_no = e.emp_no inner join departments d on d.dept_no = de.dept_no where e.last_name like '%abne%'"
