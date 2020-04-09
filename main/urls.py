from django.urls import path

from main import views

app_name='main'
urlpatterns = [
    path("index/", views.index,name='index'),
    path("login/", views.login_form,name='login'),
    path("get_code/", views.get_code),
    path("check_user/", views.check_user),
]
