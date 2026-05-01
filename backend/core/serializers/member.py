from rest_framework import serializers
from core.models import MemberRegistration


class MemberRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model           = MemberRegistration
        fields          = '__all__'
        read_only_fields = ['is_verified', 'created_at']

    # ── Custom validators ─────────────────────────────────────────

    # def validate_id_number(self, value: str) -> str:
    #     if MemberRegistration.objects.filter(id_number=value).exists():
    #         raise serializers.ValidationError(
    #             'This ID number is already registered with YR27.'
    #         )
    #     return value

    def validate_phone(self, value: str) -> str:
        if not value.startswith('0') and not value.startswith('+254'):
            raise serializers.ValidationError(
                'Enter a valid Kenyan phone number.'
            )
        return value