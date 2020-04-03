from django.urls import path
from . import views
urlpatterns = [
    path("",views.tes.as_view())
]
