from rest_framework import generics

from spacecraft import models
from . import serializers


class ListSpaceCraft(generics.ListAPIView):
    queryset = models.SpaceCraft.objects.all()
    serializer_class = serializers.SpaceCraftSerializer


class DetailSpaceCraft(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.SpaceCraft.objects.all()
    serializer_class = serializers.SpaceCraftSerializer
