from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import HouseHolds, Points, Members, Farms, Farm_points, Cropping, Crops, Seasons, Wells, Yields
from .serializers import HouseHoldSerializer, PointsSerializer, MembersSerializer, FarmsSerializer, Farm_pointsSerializer, CroppingSerializer, CropsSerializer, SeasonsSerializer, WellsSerializer, YieldsSerializer

class HouseholdsList(APIView):

    def get(self, request):
        households = HouseHolds.objects.all()
        serializer = HouseHoldSerializer(households, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class PointsList(APIView):

    def get(self, request):
        points = Points.objects.all()
        serializer = PointsSerializer(points, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class MembersList(APIView):

    def get(self, request):
        members = Members.objects.all()
        serializer = MembersSerializer(members, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class FarmsList(APIView):

    def get(self, request):
        farms = Farms.objects.all()
        serializer = FarmsSerializer(farms, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class Farm_pointsList(APIView):

    def get(self, request):
        farm_points = Farm_points.objects.all()
        serializer = Farm_pointsSerializer(farm_points, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class CroppingList(APIView):

    def get(self, request):
        cropping = Cropping.objects.all()
        serializer = CroppingSerializer(cropping, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class CropsList(APIView):

    def get(self, request):
        crops = Crops.objects.all()
        serializer = CropsSerializer(crops, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class SeasonsList(APIView):

    def get(self, request):
        seasons = Seasons.objects.all()
        serializer = HouseHoldSerializer(seasons, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class WellsList(APIView):

    def get(self, request):
        wells = Wells.objects.all()
        serializer = WellsSerializer(wells, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class YieldsList(APIView):

    def get(self, request):
        yields = Yields.objects.all()
        serializer = HouseHoldSerializer(yields, many=True)
        return Response(serializer.data)

    def post(self):
        pass





