from django.urls import path
from .views import *


def welcome():
    return "Welcome to Cntify !"


urlpatterns = [
    path("", welcome),
]
