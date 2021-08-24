from django.urls import path
from .views import (
   PodcastListView
)


urlpatterns = [
   path('podcast/',PodcastListView.as_view(),name='podcast'),
]