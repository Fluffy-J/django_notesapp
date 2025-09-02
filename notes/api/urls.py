from django.urls import path

from notes.views import HelloWorldView
from notes.views import TitleListCreate
from notes.views import NoteCreate
from notes.views import NoteUpdate
from notes.views import NoteDelete

app_name = 'notes'
urlpatterns = [
   path('hello/', HelloWorldView.as_view(), name='hello-world'),
   path('log/', TitleListCreate.as_view(), name='note-list'),
   path('makenote/', NoteCreate.as_view(),name='create'),
   path('updatenote/<int:pk>/', NoteUpdate.as_view(), name='update-note'),
   path('noteDelete/<int:id>/', NoteDelete.as_view(),name='delete-note'),
]