from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from location.models import Country
from movie.serializers import MovieListSerializer
from .serializers import CountrySerializer


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (permissions.AllowAny,)

    @action(detail=True, methods=['get'])
    def movies(self, request, pk=None):
        country = self.get_object()
        movies = country.movie_set.all()

        page = self.paginate_queryset(movies)
        if page is not None:
            serializer = MovieListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
