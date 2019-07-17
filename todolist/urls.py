from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo', views.addnewtodo, name='addtodo'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('delete_all/', views.delete_all, name='delete_all'),
    path('update/<int:pk>/', views.update_status, name='update_status'),
]
