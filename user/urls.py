from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import CurrentUserView, UserCreateAPIView


router = DefaultRouter()

urlpatterns = [
    path('me/', CurrentUserView.as_view()),
    path('users/', UserCreateAPIView.as_view()),
    *router.urls
]
