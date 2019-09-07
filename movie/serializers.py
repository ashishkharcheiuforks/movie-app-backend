from rest_framework import serializers

from artist.serializers import ArtistNoJobsSerializer, JobSerializer
from location.serializers import CountrySerializer
from movie.models import Genre, Movie, Comment, MovieArtist


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug')


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'country', 'image', 'release_date', 'genres')


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'name', 'slug', 'country', 'image', 'release_date', 'genres')


class MovieBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'name', 'slug', 'image')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'star')


class CommentListSerializer(serializers.ModelSerializer):
    movie = MovieBasicSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'movie', 'user', 'comment', 'created_at')


class MovieArtistSerializer(serializers.ModelSerializer):
    artist = ArtistNoJobsSerializer()
    job = JobSerializer()

    class Meta:
        model = MovieArtist
        fields = ('artist', 'job')
