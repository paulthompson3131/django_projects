from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path("", views.MainMenuView.as_view(), name="mainmenu"),
    path("first_url/<int:pk>", views.FirstView.as_view(), name="first_url"),
    path("second_url/<int:pk>", views.SecondView.as_view(), name="second_url"),
    path("third_url/<int:pk>", views.ThirdView.as_view(), name="third_url"),
    path("dosomething/<int:pk>", views.DoSomethingView.as_view(), name="dosomething"),
    path("employeesbysurname/<int:pk>", views.getEmployeesBySurnameView, name="employeesbysurname"),
    path("employeesbydepartment/<int:pk>", views.getEmployeesByDepartmentView, name="employeesbydepartment"),
    path("employeesbysalary/<int:pk>", views.getEmployeesBySalaryView, name="employeesbysalary"),
]