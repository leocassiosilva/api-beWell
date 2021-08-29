from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from .models import Podcast
from podcasts.serializer import PodcastSerializer
from rest_framework.permissions import IsAuthenticated


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


#List view para todos os usuarios    
class PodcastListViewUser(ListAPIView):
    permission_classes = (IsAuthenticated, )
    #queryset = CustomUsuario.objects.all()
    serializer_class = PodcastSerializer

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Podcast.objects.order_by('nome').filter(id_usuario=self.request.user)


#List view para todos os usuarios
class PodcastListView(ListModelMixin, GenericAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)