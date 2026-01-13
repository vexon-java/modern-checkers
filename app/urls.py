from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkers, name='checkers'),
]
