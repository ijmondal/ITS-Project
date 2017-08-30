from __future__ import unicode_literals

from django.db import models

class HouseHolds(models.Model):
    text = models.CharField(max_length=20)
    location_id=models.ForeignKey('Points')
    Monthly_income = models.FloatField()

    def __str__(self):
        return self.text
class Points(models.Model):
    lat=models.FloatField()
    long=models.FloatField()

class Members(models.Model):
    Name=models.CharField(max_length=30)
    Dob = models.DateField()
    Gender = models.CharField(max_length=2)

class Farms(models.Model):
    Area=models.FloatField()
    household_id = models.ForeignKey('HouseHolds')

class Farm_points(models.Model):
    farm_id = models.ForeignKey('Farms')
    point_id = models.ForeignKey('Points')
    sequence_number = models.FloatField()

class Cropping(models.Model):
    farm_id = models.ForeignKey('Farms')
    season_id=models.ForeignKey('Seasons')
    crop_id=models.ForeignKey('Crops')

class Crops(models.Model):
    Name = models.CharField(max_length=30)

class Seasons(models.Model):
    Name = models.CharField(max_length=10)

class Wells(models.Model):
    point_id=models.ForeignKey('Points')
    Depth = models.FloatField()

class Yields(models.Model):
    well_id = models.ForeignKey('Wells')
    yields = models.FloatField()
    date_last_recorded = models.DateField()





