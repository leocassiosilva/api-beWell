from rest_framework import viewsets
from .models import Podcast
from podcasts.serializer import PodcastSerializer


class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
