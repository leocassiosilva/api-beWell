from django.urls import path
from .views import (
   UsuarioListView
)


urlpatterns = [
   path('meus-dados/',UsuarioListView.as_view(),name='meus-dados'),
]