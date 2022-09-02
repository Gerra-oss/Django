from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from accounts import views

urlpatterns = [

    path('', views.login, name = 'login'),
    path('', views.logout, name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('dashboard/', views.index, name = 'dashboard'),
    path('apilist/', views.api_list, name = 'apilist/'),
    path('api/<int:id>/', views.detail),
    path('admin/', admin.site.urls),
]
urlpatterns = format_suffix_patterns(urlpatterns)
