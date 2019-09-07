from rest_framework.routers import DefaultRouter

from .views import ArtistViewSet, JobViewSet

router = DefaultRouter()
router.register('artists', ArtistViewSet)
router.register('jobs', JobViewSet)

urlpatterns = router.urls
