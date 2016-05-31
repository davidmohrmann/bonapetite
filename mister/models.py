import datetime

from django.db import models
from django.utils import timezone


class Collector(models.Model):
    # temperature=models.DecimalField(max_digits=4, decimal_places=2)
    ph_level=models.DecimalField(max_digits=4, decimal_places=2)
    time_collected=models.DateTimeField(auto_now_add=True)
   
   