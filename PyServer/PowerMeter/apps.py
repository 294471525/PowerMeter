import threading
import time

from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules




class PowermeterConfig(AppConfig):
    name = 'PowerMeter'
