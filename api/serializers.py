from rest_framework import serializers

from api.models import Timer


class TimerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timer
        fields = '__all__'
