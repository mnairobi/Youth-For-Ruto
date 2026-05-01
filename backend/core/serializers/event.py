from rest_framework import serializers
from core.models import Event


class EventSerializer(serializers.ModelSerializer):

    county_name = serializers.CharField(
        source='county.name',
        read_only=True,
        default='',
    )

    class Meta:
        model  = Event
        fields = '__all__'