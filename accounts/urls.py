from django.urls import path
from .views import (
   UsuarioListView, UsuarioCreateViewSet
)


urlpatterns = [
   path('meus-dados/', UsuarioListView.as_view(), name='meus-dados'),
   path('create/', UsuarioCreateViewSet.as_view(), name='create'),

]