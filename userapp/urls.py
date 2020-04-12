from django.urls import path
from userapp import views

app_name="userapp"
urlpatterns = [
    path("user_page/", views.user_page),
    path("get_all_user/", views.get_all_user),
    path("map_updata/", views.map_updata),
    path("load_map/", views.load_map),

]
