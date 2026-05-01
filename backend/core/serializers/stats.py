from rest_framework import serializers


class StatsSerializer(serializers.Serializer):
    total_members  = serializers.IntegerField()
    total_counties = serializers.IntegerField()
    total_events   = serializers.IntegerField()
    total_leaders  = serializers.IntegerField()