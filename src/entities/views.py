from django.shortcuts import render
from rest_framework import viewsets
from .models import Divinity
from .serializers import DivinitySerializer


class DivinityViewSet(viewsets.ModelViewSet):
    queryset = Divinity.objects.all()
    serializer_class = DivinitySerializer
