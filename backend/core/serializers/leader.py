from rest_framework import serializers
from core.models import Leader


class LeaderSerializer(serializers.ModelSerializer):

    county_name   = serializers.CharField(
        source='county.name',
        read_only=True,
        default='',
    )
    display_title = serializers.ReadOnlyField()

    class Meta:
        model  = Leader
        fields = '__all__'