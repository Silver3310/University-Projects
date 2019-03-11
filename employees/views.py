from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from datetime import date

from .models import Employee
from .forms import EmployeeForm


class EmployeesList(ListView):

    template_name = 'employees/list.html'
    queryset = Employee.objects.all()
    context_object_name = 'employees'


class EmployeeCount(ListView):

    template_name = 'employees/list.html'

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        for each in employees:
            today = date.today()
            each.age = (today.year
                        - each.birthday.year
                        - ((today.month, today.day) <
                           (each.birthday.month, each.birthday.day)))
        ctx = {
            'employees': employees,
            'ages': True
        }
        return render(request, self.template_name, ctx)


class EditEmployee(UpdateView):
    """Edit employees"""

    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/edit.html'
    success_url = reverse_lazy('list')


class CreateEmployee(CreateView):
    """Create employees"""

    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/edit.html'
    success_url = reverse_lazy('list')


def pay_for_work(request, pk):
    """Pay for the employee's work"""

    employee = Employee.objects.get(id=pk)
    employee.pay_salary()
    return HttpResponseRedirect(reverse('list'))


def fire_employee(request, pk):
    """Fire an employee"""

    employee = Employee.objects.get(id=pk)
    employee.delete()
    return HttpResponseRedirect(reverse('list'))
