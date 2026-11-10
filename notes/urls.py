from django.urls import path
from . import views

urlpatterns = [
path('', views.notes_list, name='notes_list'),
path('nova/', views.create_note, name='create_note'),
path('beleske/<int:note_id>/', views.note_detail, name='note_detail'),
path('beleske/<int:note_id>/obrisi/', views.delete_note, name='delete_note'
),
]