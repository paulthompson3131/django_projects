from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path("", views.MainMenuView.as_view(), name="mainmenu"),
    path("first_url/<int:pk>", views.FirstView.as_view(), name="first_url"),
    path("second_url/<int:pk>", views.SecondView.as_view(), name="second_url"),
    path("third_url/<int:pk>", views.ThirdView.as_view(), name="third_url"),
    path("dosomething/<int:pk>", views.getEmployeesView, name="dosomething"),
    path("getemployees/<int:pk>", views.getEmployeesBySurnameView, name="getemployees"),
    path("getemployeesurname/<int:pk>", views.GetEmployeeSurname.as_view(), name="getemployeesurname"),
    path("employeedepartment/<int:pk>", views.GetEmployeesDepartmentView.as_view(), name="employeedepartment"),
]