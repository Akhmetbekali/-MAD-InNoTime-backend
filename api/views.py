import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Timer
from api.serializers import TimerRequestSerializer


@csrf_exempt
def timers_list(request):
    if request.method == 'GET':
        timers = Timer.objects.all()
        serializer = TimerRequestSerializer(timers, many=True)
        return JsonResponse([t["json"] for t in serializer.data], safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TimerRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def timer_detail(request, pk):
    try:
        timer = Timer.objects.get(pk=pk)
    except Timer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TimerRequestSerializer(timer)
        return JsonResponse(serializer.data["json"], safe=False)

