from rest_framework import serializers
from core.models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Subscriber
        fields = ['email', 'phone']

    def validate_email(self, value: str) -> str:
        if Subscriber.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'This email is already subscribed.'
            )
        return value