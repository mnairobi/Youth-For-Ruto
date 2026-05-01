from rest_framework import serializers
from core.models import AgendaItem


class AgendaItemSerializer(serializers.ModelSerializer):

    class Meta:
        model  = AgendaItem
        fields = '__all__'