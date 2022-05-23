from turtle import update
from django.contrib import admin
from django.urls import path
from . import views 
from django.views.generic.base import TemplateView
urlpatterns = [
    path('emp', views.emp),
    path('showemp/', views.showemp),
    path('showteam/', views.showteam),
    path('manager_details', views.manager_details),
    path('deleteEmp/<str:id_carte>/', views.deleteEmp), 
    path('update/<str:id_carte>/', views.update,name='Update'),
    path('update/<str:id_carte>/updateEmp/', views.updateEmp),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]