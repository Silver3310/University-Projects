"""university_projects URL Configuration

The `urlpatterns` list routes URLs to views of the letter recognition app.
"""

from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.MainPage.as_view(),
        name="main"
    ),
    path(
        'recognize/',
        views.RecognizeLetter.as_view(),
        name="recognize"
    )
]
