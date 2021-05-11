from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import JsonResponse
from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from Swyft import settings
from trial.models import Car

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@csrf_exempt
def add_car(request):
    msg, car_id, status = '', '', ''
    if request.method == 'POST':
        try:
            car = Car()
            car.type = str(request.POST.get('car_type', False))
            car.model = str(request.POST.get('car_model', False))
            car.make = str(request.POST.get('car_make', False))
            car.price = float(request.POST.get('car_price', False))
            car.year = str(request.POST.get('car_year', False))
            car.save()
            car_id = car.id
            status = 'Success'
            msg = 'Added Successfully'
        except Exception as e:
            status = 'Failed'
            msg = f'Error is  {e}'
    else:
        status = 'Failed'
        msg = 'POST request is allowed Only'
    response = {
        'status': status,
        'msg': msg,
        'car_id': car_id

    }
    return JsonResponse(response)


@csrf_exempt
def find_car(request):
    msg, status, car_data = '', '', ''
    if request.method == 'POST':
        car_id = int(request.POST.get('car_id', False))
        if car_id:
            try:
                if car_id in cache:
                    print('In cache')
                    car_data = cache.get(car_id)
                    status = 'Success'
                    msg = 'Data Found'
                    car_data = car_data
                    print(car_data)
                else:
                    car_data = Car.objects.get(id=car_id)
                    # print(car_data)
                    status = 'Success'
                    msg = 'Data Found'
                    car_data = {'car_id': car_data.id, 'car_type': car_data.type, 'car_model': car_data.model,
                                'car_make': car_data.make, 'car_price': car_data.price, 'car_year': car_data.year, }
                    cache.set(car_id, car_data, timeout=CACHE_TTL)
            except Exception as e:
                status = 'Failed'
                msg = f'Error is  {e}'
        else:
            status = 'Failed'
            msg = 'Id is Required'
    else:
        status = 'Failed'
        msg = 'POST request is allowed Only'
    response = {
        'status': status,
        'msg': msg,
        'car_data': car_data

    }
    return JsonResponse(response)


@csrf_exempt
def del_car(request):
    msg, status, car_data = '', '', ''
    if request.method == 'POST':
        car_id = int(request.POST.get('car_id', False))
        if car_id:
            try:

                car_data = Car.objects.get(id=car_id)
                car_data.delete()
                status = 'Success'
                msg = f'Car id {car_id} Deleted Successfully '
            except Exception as e:
                status = 'Failed'
                msg = f'Error is  {e}'
        else:
            status = 'Failed'
            msg = 'Id is Required'
    else:
        status = 'Failed'
        msg = 'POST request is allowed Only'
    response = {
        'status': status,
        'msg': msg,

    }
    return JsonResponse(response)


@csrf_exempt
def update_car(request):
    msg, status, car_data = '', '', ''
    if request.method == 'POST':
        car_id = int(request.POST.get('car_id', False))
        if car_id:
            try:
                car_data = Car.objects.get(id=car_id)
                if car_data:
                    car_type = str(request.POST.get('car_type', False))
                    if car_type:
                        car_data.type = car_type
                    car_model = str(request.POST.get('car_model', False))
                    if car_type:
                        car_data.model = car_model
                    car_make = str(request.POST.get('car_make', False))
                    if car_type:
                        car_data.make = car_make
                    car_price = float(request.POST.get('car_price', False))
                    if car_type:
                        car_data.price = car_price
                    car_year = str(request.POST.get('car_year', False))
                    if car_type:
                        car_data.year = car_year
                    car_data.save()
                    status = 'Success'
                    msg = 'Updated Successfully'
                    car_data = {'car_id': car_data.id, 'car_type': car_data.type, 'car_model': car_data.model,
                                'car_make': car_data.make, 'car_price': car_data.price, 'car_year': car_data.year, }
                else:
                    status = 'Failed'
                    msg = 'Id Not Exist'
            except Exception as e:
                status = 'Failed'
                msg = f'Error is  {e}'
        else:
            status = 'Failed'
            msg = 'Id is Required'
    else:
        status = 'Failed'
        msg = 'POST request is allowed Only'
    response = {
        'status': status,
        'msg': msg,
        'car_data': car_data

    }
    return JsonResponse(response)
