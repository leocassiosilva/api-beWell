from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import  ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.models import CustomUsuario
from accounts.serializer import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = CustomUsuario.objects.all()
    serializer_class = UsuarioSerializer


#List view para todos os usuarios    
class UsuarioListView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    #queryset = CustomUsuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        return CustomUsuario.objects.filter(username=self.request.user.username)

# return CustomUsuario.objects.filter(usuario=self.request.user)