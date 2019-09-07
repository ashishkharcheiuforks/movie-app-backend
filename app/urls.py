from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # Authentication
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Movie
    path('', include('artist.urls')),
    path('', include('location.urls')),
    path('', include('movie.urls')),
    path('', include('user.urls')),
    # Admin panel
    path('admin/', admin.site.urls),
]
