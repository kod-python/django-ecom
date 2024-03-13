from typing import Any
from django.db import models

# Create your models here.

class Feature(models.Model):
    
    name = models.CharField(max_length= 100)
    desc = models.CharField(max_length= 500)
    
       
    

# class Feature:
#     id: int
#     name: str
#     desc: str
#     price: float
#     is_true: bool
