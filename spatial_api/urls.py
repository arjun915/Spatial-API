from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import spatial_point_view
from .views import SpatialPointViewSet, SpatialPolygonViewSet

# urlpatterns = [
#     path("api/points/", spatial_point_view, name="spatial-point-list"),
#     path("api/points/<int:pk>/", spatial_point_view, name="spatial-point-detail"),
# ]
router = DefaultRouter()
router.register(r'spatialpoints', SpatialPointViewSet)
router.register(r'spatialpolygons', SpatialPolygonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

