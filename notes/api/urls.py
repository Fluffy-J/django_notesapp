from django.urls import path

from notes.views import HelloWorldView

app_name = 'notes'
urlpatterns = [
   path('hello/', HelloWorldView.as_view(), name='hello-world'),  
]