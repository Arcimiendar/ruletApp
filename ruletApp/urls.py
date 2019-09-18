from django.urls import path
from . import views

url_patterns = [
    path("", views.ChoseDepartmentView.as_view()),
    path("employees_list/", views.EmployeesListView.as_view(), name='employees_list'),
    path("employee/<int:pk>", views.EmployeeDetailView.as_view(), name='employee_detail'),
    path("department/<int:pk>", views.DepartmentProfilePage.as_view(), name='department_profile')
]
