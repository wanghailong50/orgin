from django.urls import path
from userapp import views

from apiapp import views


urlpatterns = [
    path("main_api/", views.main_api),
    path("register_api/", views.register_api),
    path("change_api/", views.change_api),
]
