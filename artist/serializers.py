from rest_framework import serializers

from artist.models import Artist, Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'name', 'slug')


class ArtistSerializer(serializers.ModelSerializer):
    jobs = JobSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id', 'fullname', 'slug', 'birth_date', 'image', 'age', 'jobs')


class ArtistNoJobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'fullname', 'birth_date', 'image', 'age')
