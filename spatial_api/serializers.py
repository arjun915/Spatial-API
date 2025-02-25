from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import SpatialPoint, SpatialPolygon
from rest_framework import serializers
from geopy.geocoders import Nominatim
from django.contrib.gis.geos import GEOSGeometry

# class SpatialPointSerializer(GeoFeatureModelSerializer):
#     class Meta:
#         model = SpatialPoint
#         geo_field = "location"
#         fields = ("id", "name", "location")
class SpatialPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SpatialPoint
        geo_field = "location"  # Specifies which field is spatial
        fields = ("id", "name", "location")
    
    def validate_location(self, value):
        """Ensure location is stored as a valid GEOSGeometry object"""
        if isinstance(value, dict):  # If coming as GeoJSON
            try:
                return GEOSGeometry(str(value))  # Convert GeoJSON to GEOSGeometry
            except Exception as e:
                raise serializers.ValidationError(f"Invalid geometry: {e}")
        return value
        # address = serializers.SerializerMethodField()
# class SpatialPolygonSerializer(GeoFeatureModelSerializer):
#     class Meta:
#         model = SpatialPolygon
#         geo_field = "area"
#         fields = ("id", "name", "area")
class SpatialPolygonSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SpatialPolygon
        geo_field = "area"
        fields = ("id", "name", "area")

    def validate_area(self, value):
        """Ensure area is stored as a valid GEOSGeometry object"""
        if isinstance(value, dict):  # If it's coming as GeoJSON
            try:
                return GEOSGeometry(str(value))  # Convert GeoJSON to GEOSGeometry
            except Exception as e:
                raise serializers.ValidationError(f"Invalid geometry: {e}")
        return value