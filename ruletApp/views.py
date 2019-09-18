from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView
from . import forms
from . import models


class ChoseDepartmentView(FormView):
    template_name = "ruletApp/chose_department_page.html"
    form_class = forms.ChoseDepartmentForm

    def form_valid(self, form):
        return HttpResponseRedirect(reverse_lazy('department_profile', args=[form.cleaned_data['options']]))


class EmployeesListView(ListView):
    template_name = 'ruletApp/employee_list_page.html'
    model = models.Employee


class EmployeeDetailView(DetailView):
    template_name = 'ruletApp/employee_detail_page.html'
    model = models.Employee


class DepartmentProfilePage(DetailView):
    template_name = 'ruletApp/department_profile_page.html'
    model = models.Department
