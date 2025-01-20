from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
import html
from django import forms
from .forms import MyForm, NumberOfPeopleForm

from .models import Menu, MenuContent

from django.db import connections


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
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

class getHighSalaryEployeesView(View):
    sourcedb = "employees"
    subheading = "Employees Information"
    number_of_people = 0
    sql = f"select ROW_NUMBER() over(order by salary desc) AS RANKING, e.first_name, e.last_name, e.birth_date, e.gender, e.hire_date, s.from_date, s.salary \
            from  employees e inner join salaries s on e.emp_no = s.emp_no \
            where s.salary > 105000 \
            and to_date > CURDATE() \
            order by salary desc "

    def get(self, request, pk):
        dump = dumpdata('GET', request.GET)
        context = {'dump' : dump}
        form = NumberOfPeopleForm(request.GET)
        context['subheading'] = self.subheading
        context['number_of_people'] = self.number_of_people
        context['menu_content'] = MenuContent.objects.get(id=pk)
        context["form"] = form
        if request.method == 'GET' and 'number_of_people' in request.GET:
            number_of_people = request.GET['number_of_people']
            if form.is_valid():
                number_of_people = form.cleaned_data['number_of_people']
            sql = f"{self.sql} limit {number_of_people}"
            context['sql'] = sql
            with connections[self.sourcedb].cursor() as cursor:
                cursor.execute(sql)
                context['query_count'] = cursor.rowcount
                if cursor.rowcount > 0:
                    columns = [col[0] for col in cursor.description]
                    context['rows'] = [dict(zip(columns, row)) for row in cursor.fetchall()]
                    context['columns'] = []
                    for key, val in context['rows'][0].items():
                        context['columns'].append(key)

        return render(request, 'menu/dosomething4.html', context)

class getLowSalaryEployeesView(getHighSalaryEployeesView):
    sql = f"select ROW_NUMBER() over(order by salary asc) AS RANKING, e.first_name, e.last_name, e.birth_date, e.gender, e.hire_date, s.from_date, s.salary \
            from  employees e inner join salaries s on e.emp_no = s.emp_no \
            where s.salary < 105000 \
            and to_date > CURDATE() \
            order by salary asc "

def getEmployeesView(request, pk):
    sourcedb = "employees"
    dump = dumpdata('GET', request.GET)
    context = {'dump' : dump}
    context['subheading'] = "Employees Information"
    sname = request.GET.get('sname','')
    context['length_sname'] = len(sname)
    if sname != '':
        sql = f"select e.first_name, e.last_name, e.emp_no, d.dept_name from dept_emp de inner join employees e on de.emp_no = e.emp_no inner join departments d on d.dept_no = de.dept_no where e.last_name like '%{sname}%'"
        context['sql'] = sql
        context['function'] = 'GET'
        context['default_name'] = sname
        with connections[sourcedb].cursor() as cursor:
            cursor.execute(sql)
            context['query_count'] = cursor.rowcount
            if cursor.rowcount > 0:
                columns = [col[0] for col in cursor.description]
                context['rows'] = [dict(zip(columns, row)) for row in cursor.fetchall()]
                context['columns'] = []
                for key, val in context['rows'][0].items():
                    context['columns'].append(key)

    return render(request, 'menu/dosomething2.html', context)


def getEmployeesBySurnameView(request, pk):
    sourcedb = "employees"
    dump = dumpdata('GET', request.GET)
    context = {'dump' : dump}
    context['menu_content'] = MenuContent.objects.get(id=pk)
    context['subheading'] = "Employees Information"
    sname = request.GET.get('sname','')
    context['length_sname'] = len(sname)
    form = MyForm(request.GET)
    context["form"] = form
    if form.is_valid():
        sname = form.cleaned_data['sname']
    if sname != '':
        sql = f"select e.first_name, e.last_name, e.emp_no, d.dept_name from dept_emp de inner join employees e on de.emp_no = e.emp_no inner join departments d on d.dept_no = de.dept_no where e.last_name like '%{sname}%'"
        context['sql'] = sql
        context['function'] = 'GET'
        context['default_name'] = sname
        with connections[sourcedb].cursor() as cursor:
            cursor.execute(sql)
            context['query_count'] = cursor.rowcount
            if cursor.rowcount > 0:
                columns = [col[0] for col in cursor.description]
                context['rows'] = [dict(zip(columns, row)) for row in cursor.fetchall()]
                context['columns'] = []
                for key, val in context['rows'][0].items():
                    context['columns'].append(key)

    return render(request, 'menu/dosomething3.html', context)


def getEmployeesBySalaryView(request, pk):
    sourcedb = "employees"
    dump = dumpdata('GET', request.GET)
    context = {'dump' : dump}
    context['menu_content'] = MenuContent.objects.get(id=pk)
    context['subheading'] = "Employees Information"
    sname = request.GET.get('sname','')
    context['length_sname'] = len(sname)
    form = MyForm(request.GET)
    context["form"] = form
    if form.is_valid():
        sname = form.cleaned_data['sname']
    if sname != '':
        sql = f"select e.first_name, e.last_name, e.emp_no, s.salary \
        from employees e \
        inner join salaries s on s.emp_no = e.emp_no \
        where e.last_name like '%{sname}%'"
        context['sql'] = sql
        context['function'] = 'GET'
        context['default_name'] = sname
        with connections[sourcedb].cursor() as cursor:
            cursor.execute(sql)
            context['query_count'] = cursor.rowcount
            if cursor.rowcount > 0:
                columns = [col[0] for col in cursor.description]
                context['rows'] = [dict(zip(columns, row)) for row in cursor.fetchall()]
                context['columns'] = []
                for key, val in context['rows'][0].items():
                    context['columns'].append(key)

    return render(request, 'menu/dosomething3.html', context)


def getEmployeesByDepartmentView(request, pk):
    sourcedb = "employees"
    dump = dumpdata('GET', request.GET)
    context = {'dump' : dump}
    context['menu_content'] = MenuContent.objects.get(id=pk)
    context['subheading'] = "Employees Information"
    sname = request.GET.get('sname','')
    context['length_sname'] = len(sname)
    form = MyForm(request.GET)
    context["form"] = form
    if form.is_valid():
        sname = form.cleaned_data['sname']
    if sname != '':
        sql = f"select e.first_name, e.last_name, e.emp_no, d.dept_name from dept_emp de inner join employees e on de.emp_no = e.emp_no inner join departments d on d.dept_no = de.dept_no where e.last_name like '%{sname}%'"
        context['sql'] = sql
        context['function'] = 'GET'
        context['default_name'] = sname
        with connections[sourcedb].cursor() as cursor:
            cursor.execute(sql)
            context['query_count'] = cursor.rowcount
            if cursor.rowcount > 0:
                columns = [col[0] for col in cursor.description]
                context['rows'] = [dict(zip(columns, row)) for row in cursor.fetchall()]
                context['columns'] = []
                for key, val in context['rows'][0].items():
                    context['columns'].append(key)

    return render(request, 'menu/dosomething3.html', context)
