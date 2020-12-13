from rest_framework import serializers

from api.models import Timer


class TimerRequestSerializer(serializers.Serializer):
    json = serializers.JSONField()

    def create(self, validated_data):
        return Timer.objects.create(**validated_data)
