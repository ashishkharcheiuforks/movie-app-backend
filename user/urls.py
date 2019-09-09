from django.urls import path

from .views import CurrentUserView, UserCreateAPIView

urlpatterns = [
    path('', UserCreateAPIView.as_view()),
    path('me/', CurrentUserView.as_view()),
]
