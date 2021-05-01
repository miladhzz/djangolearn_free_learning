from django.urls import path
from . import views

app_name = "cvbs"

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/add/', views.CreateUser.as_view(), name="create_user"),
    path('users/detail/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
]
