from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    weight = models.IntegerField()
    age = models.IntegerField(blank=True, null=True)