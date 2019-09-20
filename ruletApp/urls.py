from django.urls import path
from . import views

url_patterns = [
    path("", views.ChoseDepartmentView.as_view()),
    path("employees_list/", views.EmployeesListView.as_view(), name='employees_list'),
    path("employee/<int:pk>", views.EmployeeDetailView.as_view(), name='employee_detail'),
    path("department/<int:pk>", views.DepartmentProfilePageView.as_view(), name='department_profile'),
    path("rulet/<int:pk>", views.RuletView.as_view(), name='rulet_page'),
    path("department/<int:pk>/operation/<str:operation>", views.DepartmentOperationsRedirectView.as_view(),
         name='department_operations'),

]
