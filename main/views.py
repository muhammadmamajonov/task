
from datetime import datetime
import time
from .models import Data, Apparat, Phone
from django.db.models import Q
from django.http import HttpResponse, JsonResponse


def data_analisis(request):
    
    datas = Data.objects.all()
    apparats = Apparat.objects.all()

    min_nor_time = datetime(2022,7,14,4,55)
    max_nor_time = datetime(2022,7,15,5,5)

    min_time = int(time.mktime(min_nor_time.timetuple()))
    max_time = int(time.mktime(max_nor_time.timetuple()))
    max_time -= 18000

    for t in range(min_time, max_time, 300):
        number_of_phones = datas.filter(Q(apparat_id=apparats[0].apparat_id), Q(packet_time__gt = t), Q(packet_time__lte = t+300)).count()
        Phone.objects.create(apparat=apparats[0], device_count=number_of_phones, counted_at=datetime.fromtimestamp(t+300))

        number_of_phones = datas.filter(Q(apparat_id=apparats[1].apparat_id) & Q(packet_time__gt = t) & Q(packet_time__lte = t+300)).count()
        Phone.objects.create(apparat=apparats[1], device_count=number_of_phones, counted_at=datetime.fromtimestamp(t+300))

    return HttpResponse(f"ma'lumotlar analiz qilindi")


def data_analisis_result(request):
    apparats = Apparat.objects.all()
    phones = Phone.objects.all()
    result = {}
    

    for apparat in apparats:
        dt = {}
        for data in apparat.phone_set.all():
            dt.update({f"{data.counted_at}":data.device_count})

        result.update({f"{apparat.apparat_id}":dt})

    return JsonResponse(result)

def get_one_data(request, apparat_id, counted_at):

    data = Phone.objects.get(apparat__apparat_id=apparat_id, counted_at=counted_at)
    return JsonResponse({"apparat_id":apparat_id, 'counted_at':counted_at, 'count':data.device_count})
