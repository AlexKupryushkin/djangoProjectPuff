from django.urls import path, include, re_path
from . import views
from rest_framework.routers import DefaultRouter


# /api/v0/

router = DefaultRouter()

router.register("divans", views.DivanControlViewSet)
router.register("orders", views.OrderControlViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),

    path('auth-dj/', include('djoser.urls')),
    re_path(r'^auth-dj/', include('djoser.urls.authtoken')),
]