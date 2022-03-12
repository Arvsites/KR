from django.db import models


class AircondData(models.Model):
    time = models.DateTimeField()
    t1 = models.SmallIntegerField(blank=True, null=True)
    t2 = models.SmallIntegerField(blank=True, null=True)
    t3 = models.SmallIntegerField(blank=True, null=True)
    t4 = models.SmallIntegerField(blank=True, null=True)
    t5 = models.SmallIntegerField(blank=True, null=True)
    pressure = models.SmallIntegerField(blank=True, null=True)
    c1 = models.SmallIntegerField(blank=True, null=True)
    c2 = models.SmallIntegerField(blank=True, null=True)
    current = models.SmallIntegerField(blank=True, null=True)
    client_login = models.CharField(max_length=255)
