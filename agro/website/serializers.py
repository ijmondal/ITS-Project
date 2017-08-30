from rest_framework import serializers
from .models import HouseHolds, Points, Members, Farms, Farm_points, Cropping, Crops, Seasons, Wells, Yields

class HouseHoldSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseHolds
        fields = '__all__'

class PointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Points
        fields = '__all__'

class MembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = '__all__'

class FarmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farms
        fields = '__all__'

class Farm_pointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm_points
        fields = '__all__'

class CroppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cropping
        fields = '__all__'

class CropsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crops
        fields = '__all__'

class SeasonsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seasons
        fields = '__all__'


class WellsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wells
        fields = '__all__'

class YieldsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Yields
        fields = '__all__'


































































































