from django.contrib.auth.models import User

from django.db import models


class Airconddata(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField()
    t1 = models.SmallIntegerField(blank=True, null=True)
    t2 = models.SmallIntegerField(blank=True, null=True)
    t3 = models.SmallIntegerField(blank=True, null=True)
    t4 = models.SmallIntegerField(blank=True, null=True)
    t5 = models.SmallIntegerField(blank=True, null=True)
    pressure = models.SmallIntegerField(blank=True, null=True)
    current = models.SmallIntegerField(blank=True, null=True)

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    telegram_chat_id = models.BigIntegerField(blank=True, null=True)

    cond_id = models.SmallIntegerField(blank=True, null=True)
    airconds_count = models.SmallIntegerField(blank=True, null=True)


class Person(models.Model):
    """One-to-one model to add telegram id for a user"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_chat_id = models.BigIntegerField(blank=True, null=True)
