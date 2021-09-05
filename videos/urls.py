from django.urls import path
from .views import (
   VideosListView,
   VideosListViewUser
)


urlpatterns = [
   path('videos/', VideosListView.as_view(),name='videos'),
   path('meus-videos/', VideosListViewUser.as_view(), name='meus-videos')
]