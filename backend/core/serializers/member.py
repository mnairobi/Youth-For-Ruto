from rest_framework import serializers
from core.models import MemberRegistration


class MemberRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model            = MemberRegistration
        fields           = '__all__'
        read_only_fields = ['is_verified', 'created_at']

    def validate_phone(self, value: str) -> str:
        cleaned = value.strip()
        if not cleaned.startswith('0') and not cleaned.startswith('+254'):
            raise serializers.ValidationError(
                'Enter a valid Kenyan phone number starting with 0 or +254.'
            )
        return cleaned