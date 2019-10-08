from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'DES_FUNCTION'
urlpatterns = [
    path('', views.index,name='index'),
    path('encrypt/',views.encrypt,name='encrypt'),
    path('decrypt/',views.decrypt,name='decrypt'),
]
