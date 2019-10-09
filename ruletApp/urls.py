from django.urls import path
from . import views

url_patterns = [
    # path("", views.ReactFrontView.as_view()),
    path("", views.ChoseDepartmentView.as_view(), name='home'),
    path("employees_list/", views.EmployeesListView.as_view(), name='employees_list'),
    path("employee/<int:pk>", views.EmployeeDetailView.as_view(), name='employee_detail'),
    path("department/<int:pk>", views.DepartmentProfilePageView.as_view(), name='department_profile'),
    path("rulet/<int:pk>", views.RuletView.as_view(), name='rulet_page'),
    path("department/<int:pk>/operation/<str:operation>", views.DepartmentOperationsRedirectView.as_view(),
         name='department_operations'),
    path("rulet/list", views.RuletSessionListView.as_view(), name='rulet_session_list'),
    path("rulet/list/<int:pk>", views.RuletSessionResultView.as_view(), name='rulet_result'),
]
