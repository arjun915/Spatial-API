from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

from .models import SpatialPoint, SpatialPolygon
from .serializers import SpatialPointSerializer, SpatialPolygonSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from django.contrib.gis.geos import GEOSGeometry
from django.http import JsonResponse

# @csrf_exempt
# def spatial_point_view(request, pk=None):
#     if request.method == "GET":
#         if pk:
#             # Retrieve a single spatial point
#             try:
#                 point = SpatialPoint.objects.get(pk=pk)
#                 serializer = SpatialPointSerializer(point)
#                 return JsonResponse(serializer.data, safe=False)
#             except ObjectDoesNotExist:
#                 return JsonResponse({"error": "Point not found"}, status=404)
#         else:
#             # Retrieve all spatial points
#             points = SpatialPoint.objects.all()
#             serializer = SpatialPointSerializer(points, many=True)
#             return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         # Create a new spatial point
#         data = JSONParser().parse(request)
#         geojson_data = data.get("geometry")

#         if geojson_data:
#             try:
#                 geometry = GEOSGeometry(str(geojson_data))
#                 data["location"] = geometry  # Assuming 'location' is the model field
#             except Exception as e:
#                 return JsonResponse({"error": str(e)}, status=400)

#         serializer = SpatialPointSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({"message": "Point Created Successfully", "data": serializer.data}, status=201)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "PUT":
#         # Update an existing spatial point
#         if not pk:
#             return JsonResponse({"error": "Point ID required for update"}, status=400)

#         try:
#             point = SpatialPoint.objects.get(pk=pk)
#         except ObjectDoesNotExist:
#             return JsonResponse({"error": "Point not found"}, status=404)

#         data = JSONParser().parse(request)
#         geojson_data = data.get("geometry")

#         if geojson_data:
#             try:
#                 geometry = GEOSGeometry(str(geojson_data))
#                 data["location"] = geometry
#             except Exception as e:
#                 return JsonResponse({"error": str(e)}, status=400)

#         serializer = SpatialPointSerializer(point, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({"message": "Point Updated Successfully", "data": serializer.data}, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == "DELETE":
#         # Delete a spatial point
#         if not pk:
#             return JsonResponse({"error": "Point ID required for deletion"}, status=400)

#         try:
#             point = SpatialPoint.objects.get(pk=pk)
#             point.delete()
#             return JsonResponse({"message": "Point deleted successfully"}, status=204)
#         except ObjectDoesNotExist:
#             return JsonResponse({"error": "Point not found"}, status=404)

#     else:
#         return JsonResponse({"error": "Method not allowed"}, status=405)


class SpatialPointViewSet(viewsets.ModelViewSet):
    queryset = SpatialPoint.objects.all()
    serializer_class = SpatialPointSerializer

class SpatialPolygonViewSet(viewsets.ModelViewSet):
    queryset = SpatialPolygon.objects.all()
    serializer_class = SpatialPolygonSerializer

