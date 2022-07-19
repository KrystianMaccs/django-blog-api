from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)

from apps.users.views import SignupView, UserDetailView

from apps.users.views import *
from apps.posts.views import PostViewSet


router = DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", SignupView.as_view(), name="signup"),
    path("user/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/obtain/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("", include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)