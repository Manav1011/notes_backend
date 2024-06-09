from django.urls import path,re_path
from .views import CreateNoteView,ListNotesView,GetDeleteUpdateNotes

app_name='Notes'

urlpatterns=[
    path('',ListNotesView,name='ListNotesView'),
    re_path(r'CreateNote/',CreateNoteView,name='CreateNoteView'),
    path('GetDeleteUpdateNotes/<int:pk>',GetDeleteUpdateNotes,name='GetDeleteUpdateNotes'),
]