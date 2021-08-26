from django.urls import path
from rest_framework import views
from .views import (
   UsuarioListView, UsuarioCreateViewSet
)


urlpatterns = [
   path('meus-dados/', UsuarioListView.as_view(), name='meus-dados'),
   path('cadastro/', UsuarioCreateViewSet.as_view(), name='cadastro'),

]