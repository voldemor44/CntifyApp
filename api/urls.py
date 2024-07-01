from django.urls import path
from .controllers.basics_crud import *


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

    path("advertising/", AdvertisingViewset.as_view()),
    path("advertising/<int:id>", AdvertisingViewset.as_view()),

    path("newsletters/", NewslettersViewset.as_view()),
    path("newsletters/<int:id>", NewslettersViewset.as_view()),

    path("notifications/", NotificationsViewset.as_view()),
    path("notifications/<int:id>", NewslettersViewset.as_view()),
]