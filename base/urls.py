from django.urls import path
from . import views

urlpatterns = [
      path('login/', views.loginPage, name='login'),
      path('logout/', views.logoutUser, name='logout'),
      path('register/', views.registerPage, name='register'),
      path('', views.home, name='home'),
      path('create-task/', views.createTask, name='create-task'),
      path('update-task/<str:pk>/', views.updateTask, name='update-task'),
      path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),
]
