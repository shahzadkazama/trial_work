import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Swyft.settings")
django.setup()
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.http import JsonResponse
from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from Swyft import settings
from trial.models import Car

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


# cache.set(str(1), 'hi', timeout=CACHE_TTL)
car_data = cache.get('1')


print(car_data)
cache.clear()