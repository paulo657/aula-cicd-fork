from django.shortcuts import render
from .models import Songs
from rest_framework import generics
from .serializers import SongSerializer


class SongCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Songs.objects.all()
    serializer_class = SongSerializer


class SongList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

class SongDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

class SongUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

class SongDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

