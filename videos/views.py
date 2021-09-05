from rest_framework import viewsets
from .models import Video
from videos.serializer import VideoSerializer
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated

class VideoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Video.objects.all()
    serializer_class = VideoSerializer



#Lista os podcasts daquele usuarios    
class VideosListViewUser(ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.order_by('nome').filter(id_usuario=self.request.user)


#List view para todos os usuarios
class VideosListView(ListModelMixin, GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)

