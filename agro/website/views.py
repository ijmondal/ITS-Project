from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import HouseHolds, Points, Members, Farms, Farm_points, Cropping, Crops, Seasons, Wells, Yields
from .serializers import HouseHoldSerializer, PointsSerializer, MembersSerializer, FarmsSerializer, Farm_pointsSerializer, CroppingSerializer, CropsSerializer, SeasonsSerializer, WellsSerializer, YieldsSerializer

class HouseholdsList(viewsets.ModelViewSet):
    queryset = HouseHolds.objects.all()
    serializer_class = HouseHoldSerializer

    # def get(self, request):
        # households = HouseHolds.objects.all()
        # serializer = HouseHoldSerializer(households, many=True)
        # return Response(serializer.data)


    # def post(self):
    #     pass

class PointsList(viewsets.ModelViewSet):
    queryset = Points.objects.all()
    serializer_class = PointsSerializer

    # def get(self, request):
    #     points = Points.objects.all()
    #     serializer = PointsSerializer(points, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass

class MembersList(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

    # def get(self, request):
    #     members = Members.objects.all()
    #     serializer = MembersSerializer(members, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass

class FarmsList(viewsets.ModelViewSet):
    queryset = Farms.objects.all()
    serializer_class = FarmsSerializer

    # def get(self, request):
    #     farms = Farms.objects.all()
    #     serializer = FarmsSerializer(farms, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass

class Farm_pointsList(viewsets.ModelViewSet):
    queryset = Farm_points.objects.all()
    serializer_class = Farm_pointsSerializer

    # def get(self, request):
    #     farm_points = Farm_points.objects.all()
    #     serializer = Farm_pointsSerializer(farm_points, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass

class CroppingList(viewsets.ModelViewSet):
    queryset = Cropping.objects.all()
    serializer_class = CroppingSerializer

    # def get(self, request):
    #     cropping = Cropping.objects.all()
    #     serializer = CroppingSerializer(cropping, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass

class CropsList(viewsets.ModelViewSet):
    queryset = Crops.objects.all()
    serializer_class = CropsSerializer
    #
    # def get(self, request):
    #     crops = Crops.objects.all()
    #     serializer = CropsSerializer(crops, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass

class SeasonsList(viewsets.ModelViewSet):
    queryset = Seasons.objects.all()
    serializer_class = SeasonsSerializer

    # def get(self, request):
    #     seasons = Seasons.objects.all()
    #     serializer = HouseHoldSerializer(seasons, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass

class WellsList(viewsets.ModelViewSet):
    queryset = Wells.objects.all()
    serializer_class = WellsSerializer

    # def get(self, request):
    #     wells = Wells.objects.all()
    #     serializer = WellsSerializer(wells, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass

class YieldsList(viewsets.ModelViewSet):
    queryset = Yields.objects.all()
    serializer_class = YieldsSerializer

    # def get(self, request):
    #     yields = Yields.objects.all()
    #     serializer = HouseHoldSerializer(yields, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass





