from rest_framework import viewsets
from .models import Video
from videos.serializer import VideoSerializer


class TrabalhoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
