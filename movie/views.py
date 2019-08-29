from django.db import IntegrityError
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.response import Response

from app.permissions import IsAdminUserOrReadOnly
from .models import Movie, Genre, Comment
from .serializers import MovieSerializer, MovieListSerializer, GenreSerializer, CommentListSerializer, CommentSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return MovieListSerializer
        return MovieSerializer

    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        movie = self.get_object()
        comments = movie.comment_set.filter(confirmed=True)

        page = self.paginate_queryset(comments)
        if page is not None:
            serializer = CommentListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], permission_classes=(IsAuthenticated,))
    def set_comment(self, request, pk=None):
        movie = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            try:
                comment = Comment()
                comment.movie = movie
                comment.user = self.request.user
                comment.comment = serializer.data['comment']
                comment.save()
                return Response(serializer.data)
            except IntegrityError as error:
                print(type(error))
                return Response({'detail': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (permissions.AllowAny,)
