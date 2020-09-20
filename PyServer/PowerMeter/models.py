from django.db import models

class users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class data(models.Model):
    nodeId = models.IntegerField(default=0)
    power = models.DecimalField(max_digits=10, decimal_places=2)
    current = models.DecimalField(max_digits=10, decimal_places=2)
    voltage = models.DecimalField(max_digits=10, decimal_places=2)
    dateTime = models.DateTimeField(auto_now_add=True)

class nodes(models.Model):
    nodeId = models.AutoField(primary_key= True)
    name = models.CharField(max_length=50, null= True)