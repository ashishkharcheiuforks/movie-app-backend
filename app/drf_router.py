from rest_framework.routers import DefaultRouter

from artist.views import ArtistViewSet, JobViewSet
from location.views import CountryViewSet
from movie.views import MovieViewSet, GenreViewSet

router = DefaultRouter()
router.register('artists', ArtistViewSet)
router.register('jobs', JobViewSet)

router.register('countries', CountryViewSet)

router.register('movies', MovieViewSet)
router.register('genres', GenreViewSet)

urlpatterns = router.urls
