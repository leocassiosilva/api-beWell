from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from .models import Podcast
from podcasts.serializer import PodcastSerializer
from rest_framework.permissions import IsAuthenticated


class PodcastViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


#Lista os podcasts daquele usuarios    
class PodcastListViewUser(ListAPIView):
    serializer_class = PodcastSerializer

    def get_queryset(self):
        return Podcast.objects.order_by('nome').filter(id_usuario=self.request.user)


#List view para todos os usuarios
class PodcastListView(ListModelMixin, GenericAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)
