from django.urls import path
from . import views

app_name = "cbvs"

urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/add/', views.CreateUser.as_view(), name="create_user"),
    path('users/detail/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
    path('users/update/<int:pk>/', views.UpdateUser.as_view(), name="update_user"),

    path('info/', views.InfoList.as_view(), name="info_list"),
    path('info/detail/<int:pk>/', views.InfoDetail.as_view(), name="info_detail"),
    path('info/update/<int:pk>/', views.UpdateInfo.as_view(), name="update_info"),
    path('info/delete/<str:title>/', views.DeleteInfo.as_view(), name="delete_info"),
]
