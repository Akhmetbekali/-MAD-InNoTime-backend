from django.shortcuts import render
from rest_framework import permissions, viewsets

# Create your views here.
from api.models import Timer
from api.serializers import TimerRequestSerializer


class TimerView(viewsets.ModelViewSet):
    queryset = Timer.objects.all()
    serializer_class = TimerRequestSerializer
    permissions = [permissions.AllowAny]
