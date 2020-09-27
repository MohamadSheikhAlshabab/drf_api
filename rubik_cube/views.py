from django.shortcuts import render
from rest_framework import generics
from .models import Cube
from .serializer import CubeSerializer

class CubeList(generics.ListCreateAPIView):
    queryset = Cube.objects.all()
    serializer_class = CubeSerializer

class CubeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cube.objects.all()
    serializer_class = CubeSerializer