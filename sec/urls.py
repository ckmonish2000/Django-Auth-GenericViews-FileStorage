from django.urls import path
from . import views

urlpatterns = [
    path("ran/",views.index)
]
