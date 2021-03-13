from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    descr=models.TextField(max_length=500)
    prioirty=models.IntegerField()
    comp=models.BooleanField()
