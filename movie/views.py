from django.db import IntegrityError
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response

from app.permissions import IsAdminUserOrReadOnly
from artist.models import Artist
from artist.serializers import ArtistNoJobsSerializer
from parameter.helper import ACTOR_JOB_ID, DIRECTOR_JOB_ID
from .models import Movie, Genre, Comment
from .serializers import MovieSerializer, MovieListSerializer, GenreSerializer, CommentListSerializer, \
    CommentSerializer, MovieArtistSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    lookup_field = 'slug'

    def get_serializer_class(self):
        return MovieListSerializer if self.request.method in SAFE_METHODS else MovieSerializer

    @action(detail=True, methods=['get'])
    def comments(self, request, slug=None):
        movie = self.get_object()
        comments = movie.comment_set.filter(confirmed=True)

        page = self.paginate_queryset(comments)
        if page is not None:
            serializer = CommentListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=(IsAuthenticated,))
    def set_comment(self, request, slug=None):
        movie = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                comment = Comment()
                comment.movie = movie
                comment.user = self.request.user
                comment.comment = serializer.data['comment']
                comment.star = serializer.data['star']
                comment.save()
                return Response(serializer.data)
            except IntegrityError as error:
                return Response({'detail': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def directors(self, request, slug=None):
        if DIRECTOR_JOB_ID:
            movie = self.get_object()
            directors = Artist.objects.filter(movieartist__movie=movie, movieartist__job_id=DIRECTOR_JOB_ID)
            serializer = ArtistNoJobsSerializer(directors, many=True)
            return Response(serializer.data)
        else:
            return Response([])

    @action(detail=True, methods=['get'])
    def actors(self, request, slug=None):
        if ACTOR_JOB_ID:
            movie = self.get_object()
            actors = Artist.objects.filter(movieartist__movie=movie, movieartist__job_id=ACTOR_JOB_ID)
            serializer = ArtistNoJobsSerializer(actors, many=True)
            return Response(serializer.data)
        else:
            return Response([])

    @action(detail=True, methods=['get'])
    def artists(self, request, slug=None):
        movie = self.get_object()
        artists = movie.movieartist_set.all()
        serializer = MovieArtistSerializer(artists, many=True)
        return Response(serializer.data)


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.AllowAny,)
    lookup_field = 'slug'

    @action(detail=True, methods=['get'])
    def movies(self, request, slug=None):
        genre = self.get_object()
        movies = genre.movie_set.all()

        page = self.paginate_queryset(movies)
        if page is not None:
            serializer = MovieListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
