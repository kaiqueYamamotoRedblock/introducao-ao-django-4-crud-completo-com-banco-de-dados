from django.contrib import admin
from django.urls import path, include
from .views import index, create, edit, destroy, update

urlpatterns = [
    path('', index),
    path('save', create, name='save'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', destroy, name='delete')
]
