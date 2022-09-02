from django.urls import path
from . import views

urlpatterns =[
    path('', views.api_list, name= 'api_list'),
    path('api/<int:pk>/', views.api_detail),
]
