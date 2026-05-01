from rest_framework import serializers


class StatsSerializer(serializers.Serializer):
    """
    Read-only serializer — not bound to any model.
    Shaped in the stats() view function.
    """
    total_members    = serializers.IntegerField()
    total_counties   = serializers.IntegerField()
    total_events     = serializers.IntegerField()
    total_leaders    = serializers.IntegerField()
    total_mobilizers = serializers.IntegerField()