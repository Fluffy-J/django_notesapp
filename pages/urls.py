from django.urls import path

from . import views

appapp_name = 'notes'
urlpatterns = [
    path('', views.index, name='index'),
]