from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(
        r'^edit/(?P<pk>[\w-]+)/$',
        views.EditEmployee.as_view(),
        name='edit'
    ),
    re_path(
        r'^pay/(?P<pk>[\w-]+)/$',
        views.pay_for_work,
        name='pay-money'
    ),
    re_path(
        r'^fire/(?P<pk>[\w-]+)/$',
        views.fire_employee,
        name='fire'
    ),
    path(
        'create/',
        views.CreateEmployee.as_view(),
        name='create'
    ),
    path(
        'count/',
        views.EmployeeCount.as_view(),
        name='count'
    ),
    path(
        '',
        views.EmployeesList.as_view(),
        name='list'
    ),
]
