from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .models import Podcast
from podcasts.serializer import PodcastSerializer


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


#List view para todos os usuarios
class PodcastListView(ListModelMixin, GenericAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)