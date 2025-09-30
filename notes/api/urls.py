from django.urls import path

from notes.views import TitleListCreate
from notes.views import NoteCreate
from notes.views import NoteUpdate
from notes.views import NoteDelete
from notes.views import CreateCategory

app_name = 'notes'
urlpatterns = [
   path('log/', TitleListCreate.as_view(), name='note-list'),
   path('makenote/', NoteCreate.as_view(),name='create'),
   path('updatenote/<int:pk>/', NoteUpdate.as_view(), name='update-note'),
   path('noteDelete/<int:id>/', NoteDelete.as_view(),name='delete-note'),
   path('createcategory/', CreateCategory.as_view(),name='create-category'),
]