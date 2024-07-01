from django.urls import path
from .controllers.basics_crud import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


urlpatterns = [
    path("", welcome),
    path(
        "users/", UsersViewset.as_view()
    ),  # Represente le get_all et le post (instersion d'une ligne)
    path("users/<int:id>", UsersViewset.as_view()),  # Représente get, patch et delete
    path("partners/", PartnersViewset.as_view()),
    path("partners/<int:id>", PartnersViewset.as_view()),
    path("phonebooks/", PhonebooksViewset.as_view()),
    path("phonebooks/<int:id>", PhonebooksViewset.as_view()),
]
