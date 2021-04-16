from django.urls import path
from . import views

app_name = "cvbs"

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.UserList.as_view(), name="user_list")
]
