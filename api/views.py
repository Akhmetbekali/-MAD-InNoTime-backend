import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Timer
from api.serializers import TimerRequestSerializer

@api_view(('GET', 'POST'))
@csrf_exempt
def timers_list(request):
    if request.method == 'GET':
        timers = Timer.objects.all()
        serializer = TimerRequestSerializer(timers, many=True)
        return JsonResponse([t["json"] for t in serializer.data], safe=False)
    elif request.method == 'POST':
        a = request.body.decode("utf-8")
        serializer = TimerRequestSerializer(data=json.loads(a))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def timer_detail(request, pk):
    try:
        timer = Timer.objects.get(pk=pk)
    except Timer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TimerRequestSerializer(timer)
        return JsonResponse(serializer.data["json"], safe=False)

