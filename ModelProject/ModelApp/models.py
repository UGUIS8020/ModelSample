from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Sales(models.Model):
    fee = models.IntegerField()
    creat_at = models.DateTimeField()
    update_at = models.DateTimeField()
