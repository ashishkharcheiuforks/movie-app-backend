from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from artist.models import Artist, Job
from artist.serializers import ArtistSerializer, JobSerializer
from movie.serializers import MovieArtistNoMovieSerializer


class ArtistViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def movies(self, request, slug=None):
        artist = self.get_object()
        movies = artist.movieartist_set.all()

        page = self.paginate_queryset(movies)
        if page is not None:
            serializer = MovieArtistNoMovieSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = MovieArtistNoMovieSerializer(movies, many=True)
        return Response(serializer.data)


class JobViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.AllowAny,)

    @action(detail=True, methods=['get'])
    def artists(self, request, pk=None):
        job = self.get_object()
        artists = job.artist_set.all()

        page = self.paginate_queryset(artists)
        if page is not None:
            serializer = ArtistSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
