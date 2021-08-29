from django.urls import path
from .views import (
   PodcastListView,
   PodcastListViewUser
)


urlpatterns = [
   path('podcast/',PodcastListView.as_view(),name='podcast'),
   path('meus-podcasts/', PodcastListViewUser.as_view(), name='meus-podecasts')
]