from django.urls import path

from banner import views

app_name='banner'

urlpatterns = [
    path("get_all_banner/", views.get_all_banner),
    path("add_banner/", views.add_banner),
    path("del_data/", views.del_data,name='del_data'),
    path("change/", views.change,name='change'),
]
