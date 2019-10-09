from typing import List

from django.db.models import Q
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, TemplateView, RedirectView
from . import forms, models
from .utils import set_department_from_cookie


class ChoseDepartmentView(FormView):
    template_name = "ruletApp/chose_department_page.html"
    form_class = forms.ChoseDepartmentForm

    def form_valid(self, form):
        return HttpResponseRedirect(reverse_lazy('department_profile', args=[form.cleaned_data['options'].id]))


@set_department_from_cookie
class EmployeesListView(ListView):
    template_name = 'ruletApp/employee_list_page.html'
    model = models.Employee


@set_department_from_cookie
class EmployeeDetailView(DetailView):
    template_name = 'ruletApp/employee_detail_page.html'
    model = models.Employee


class DepartmentProfilePageView(DetailView):
    template_name = 'ruletApp/department_profile_page.html'
    model = models.Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if len(models.Department.objects.filter(Q(rulet_state=models.Department.RULET_STATE[1][0]) |
                                                Q(rulet_state=models.Department.RULET_STATE[2][0]))) > 0:
            # if there is a rulet in action
            department: models.Department = self.get_object()
            if department.rulet_state == models.Department.RULET_STATE[0][0]:  # if have not allowed yet
                context['state'] = 'needs_to_allow'
                context['message'] = 'You need to allow or/and join to the rulet.'
            elif department.rulet_state == models.Department.RULET_STATE[1][0]:  # if it is participating
                context['state'] = 'participating'
                context['message'] = 'You are participating in the rulet.'
            else:  # if it is not participating
                context['state'] = 'message'
                context['message'] = 'You are not participating in the rulet, but you still can.'
        else:  # if there is not any rulet in the action
            context['state'] = 'message'
            context['message'] = 'You can begin the rulet session.'

        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.set_cookie('department', self.object.id)
        return response


class RuletView(DetailView):
    template_name = 'ruletApp/rulet_page.html'
    model = models.Department

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = models.Employee.objects.all().filter(department=None)
        return context


class DepartmentOperationsRedirectView(RedirectView):
    """
    Do operation under selected department and redirect back to the department profile page
    Operations:
        clear - clears stuff from department
        not_rulet - not to join in the rulet
        clear_all - clears stuff from all departments;
    """

    def get_redirect_url(self, *args, **kwargs):

        if kwargs['operation'] == 'clear_all':
            for department in models.Department.objects.all():
                for employee in department.employees.all():
                    employee.department = None
                    employee.save()
            return reverse_lazy('home')

        department = get_object_or_404(models.Department, pk=kwargs['pk'])
        if kwargs['operation'] == 'clear':
            for employee in department.employees.all():
                employee.department = None
                employee.save()

        elif kwargs['operation'] == 'not_rulet':
            department.rulet_state = models.Department.RULET_STATE[2][0]  # not participate state
            department.save()
        else:
            raise Http404  # if requested operation is not supported

        return reverse_lazy('department_profile', kwargs={'pk': kwargs['pk']})


@set_department_from_cookie
class RuletSessionListView(ListView):
    template_name = 'ruletApp/rulet_list_page.html'
    model = models.RuletSession


@set_department_from_cookie
class RuletSessionResultView(DetailView):
    template_name = 'ruletApp/rulet_session_result_page.html'
    model = models.RuletSession

    def get_context_data(self, **kwargs):
        rulet_session: models.RuletSession = self.get_object()
        context = super().get_context_data(**kwargs)
        context['departments'] = set()
        dict_employees = {}
        for rulet_choice in rulet_session.rulet_choices.all():
            context['departments'].add(rulet_choice.department)
            if rulet_choice.department not in dict_employees.keys():
                dict_employees[rulet_choice.department] = []
            dict_employees[rulet_choice.department].append(rulet_choice.employee)

        context['employee_data']: List[List[models.Employee]] = []
        if len(dict_employees) == 0:
            max_len_of_employee_list = 0
        else:
            max_len_of_employee_list = max((len(employee_list) for employee_list in dict_employees.values()))
        for i in range(max_len_of_employee_list):  # prepare employee data to table representation
            context['employee_data'].append([])
            for employee_list in dict_employees.values():
                try:
                    context['employee_data'][i].append(employee_list[i])
                except IndexError:
                    context['employee_data'][i].append('')

        return context


class ReactFrontView(TemplateView):
    template_name = 'ruletApp/build/index.html'
