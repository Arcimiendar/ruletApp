from django.urls import path
from . import views

url_patterns = [
    path("", views.ReactFrontView.as_view()),
    path("employees_list/", views.ReactFrontView.as_view()),
    path("employee/<int:pk>", views.ReactFrontView.as_view()),
    path("department/<int:pk>", views.ReactFrontView.as_view()),
    path("rulet/<int:pk>", views.ReactFrontView.as_view()),
    path("rulet/list/", views.ReactFrontView.as_view()),
    path("rulet/list/<int:pk>", views.ReactFrontView.as_view()),
    path("t/", views.ChoseDepartmentView.as_view(), name='home'),
    path("t/employees_list/", views.EmployeesListView.as_view(), name='employees_list'),
    path("t/employee/<int:pk>", views.EmployeeDetailView.as_view(), name='employee_detail'),
    path("t/department/<int:pk>", views.DepartmentProfilePageView.as_view(), name='department_profile'),
    path("t/rulet/<int:pk>", views.RuletView.as_view(), name='rulet_page'),
    path("t/department/<int:pk>/operation/<str:operation>", views.DepartmentOperationsRedirectView.as_view(),
         name='department_operations'),
    path("t/rulet/list/", views.RuletSessionListView.as_view(), name='rulet_session_list'),
    path("t/rulet/list/<int:pk>", views.RuletSessionResultView.as_view(), name='rulet_result'),
]
