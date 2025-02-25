# from django.db import models
from django.contrib.gis.db import models  # ✅ Import from django.contrib.gis.db

class SpatialPoint(models.Model):
    name = models.CharField(max_length=100)
    location = models.MultiPointField()

    def __str__(self):
        return self.name

class SpatialPolygon(models.Model):
    name = models.CharField(max_length=100)
    area = models.PolygonField()

    def __str__(self):
        return self.name

# Create your models here.
