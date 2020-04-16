from django.urls import path
from userapp import views
from albumapp import views

urlpatterns = [
    path("get_album/", views.get_album),
    path("get_setcion/", views.get_setcion),
    path("add_viedo/", views.add_viedo),

]
