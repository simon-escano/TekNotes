from django.urls import path
from . import views

app_name = 'note'

urlpatterns = [
    path('new/', views.new_note, name='new_note'),
]
