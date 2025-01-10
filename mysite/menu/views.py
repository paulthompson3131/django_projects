from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
import html

from .models import Menu, MenuContent

from django.db import connections

from django import forms
from form.forms import BasicForm

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
    form = BasicForm()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ##context['heading'] = self.menu_content.label
        context['form'] = self.form
        context['menu_content'] = MenuContent.objects.get(id=self.kwargs['pk'])
        context['heading'] = "Test Heading"
        context['subheading'] = "Employees Information"
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
    sql = "SELECT emp_no,birth_date,first_name,last_name ,gender,hire_date from employees \
    where last_name like 'Tho%' and hire_date > '1996-10-10' order by last_name"


class GetEmployeesDepartmentView(DoSomethingView):
    sourcedb = "employees"
    sql = "select e.first_name, e.last_name, e.emp_no, d.dept_name \
    from dept_emp de inner join employees e on de.emp_no = e.emp_no \
    inner join departments d on d.dept_no = de.dept_no where e.last_name like '%abne%'"


class GetEmployeeSurname(TemplateView):
    template_name = 'menu/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_content'] = MenuContent.objects.get(id=self.kwargs['pk'])
        context['subheading'] = "Employees Surname"
        return context

# Call as dumpdata('GET', request.GET)
def dumpdata(place, data) :
    retval = "starting: "
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

class CatCreate(View):
    sourcedb = "employees"
    heading = "Test Heading"
    subheading = "Employees Information"

    def get(self, request, pk):
        dump = dumpdata('GET', request.GET)
        context = {'dump' : dump}
        context['function'] = 'GET'
        context['menu_content'] = pk # MenuContent.objects.get(id=self.kwargs['pk'])
        context['heading'] = self.heading
        context['subheading'] = self.subheading
        return render(request, 'menu/dosomething2.html', context)

    def post(self, request, pk):
        dump = dumpdata('POST', request.POST)
        context = {'dump' : dump}
        context['heading'] = self.heading
        context['subheading'] = self.subheading
        context['sname'] = request.POST['sname']
        sname = request.POST['sname']
        sql = f"select e.first_name, e.last_name, e.emp_no, d.dept_name from dept_emp de inner join employees e on de.emp_no = e.emp_no inner join departments d on d.dept_no = de.dept_no where e.last_name like '%{sname}%'"
        context['sql'] = sql
        context['function'] = 'POST'
        context['default_name'] = sname
        query_count=0
        with connections[self.sourcedb].cursor() as cursor:
            cursor.execute(sql)
            context['query_count'] = cursor.rowcount
            if cursor.rowcount > 0:
                columns = [col[0] for col in cursor.description]
                context['rows'] = [dict(zip(columns, row)) for row in cursor.fetchall()]
                context['columns'] = []
                for key, val in context['rows'][0].items():
                    context['columns'].append(key)
        return render(request, 'menu/dosomething2.html', context)

