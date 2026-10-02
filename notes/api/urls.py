from django.urls import path

from .views import (
    TitleListCreate,
    NoteCreate,
    NoteUpdate,
    NoteDelete,
)

app_name = 'notes_api'
urlpatterns = [
   path('log/', TitleListCreate.as_view(), name='note-list'),
   path('makenote/', NoteCreate.as_view(),name='create'),
   path('updatenote/<int:pk>/', NoteUpdate.as_view(), name='update-note'),
   path('noteDelete/<int:id>/', NoteDelete.as_view(),name='delete-note'),
]