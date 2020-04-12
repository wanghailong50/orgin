from django.urls import path
from artapp import views


app_name='artapp'
urlpatterns = [
    path("art_img/", views.art_img),
    path("art_page/", views.art_page),
    path("get_all_img/", views.get_all_img),
    path("add_art/", views.add_art),

]
