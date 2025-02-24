from django.urls import path
from . import views

urlpatterns = [
    path('',views.to_dolist, name = 'to_dolist')
]