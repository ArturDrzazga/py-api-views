from django.urls import path, include
from rest_framework import routers

from cinema.views import (GenreList,
                          GenreDetail,
                          ActorList,
                          ActorDetail,
                          CinemaHallViewSet,
                          MovieViewSet)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
urlpatterns = [
    path("genre/", GenreList.as_view(), name="genre-list"),
    path("genre/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actor/", ActorList.as_view(), name="actor-list"),
    path("actor/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinemahall/", CinemaHallViewSet.as_view(actions={
        "get": "list",
        "post": "create"
    }), name="cinemahall-list"),
    path("cinemahall/<int:pk>/", CinemaHallViewSet.as_view(actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }), name="cinemahall-detail"),
    path("movie/", include(router.urls)),
]

app_name = "cinema"
