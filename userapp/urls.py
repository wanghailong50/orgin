from django.urls import path
from userapp import views
from userapp import views

app_name='main'
urlpatterns = [
    path("user_page/", views.user_page,name='user_page'),

]
