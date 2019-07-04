from rest_framework import serializers
from spacecraft import models


class SpaceCraftSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description'
        )
        model = models.SpaceCraft
