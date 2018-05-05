# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class restaurent(models.Model):
    name = models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    review_text=models.CharField(max_length=5000)





