from rest_framework import serializers
from core.models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model  = ContactMessage
        fields = [
            'full_name',
            'email',
            'phone',
            'subject',
            'message',
        ]