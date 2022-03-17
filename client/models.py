from django.contrib.auth.models import User

from django.db import models


class ClientAirconddata(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.DateTimeField()
    t1 = models.SmallIntegerField(blank=True, null=True)
    t2 = models.SmallIntegerField(blank=True, null=True)
    t3 = models.SmallIntegerField(blank=True, null=True)
    t4 = models.SmallIntegerField(blank=True, null=True)
    t5 = models.SmallIntegerField(blank=True, null=True)
    pressure = models.SmallIntegerField(blank=True, null=True)
    current = models.SmallIntegerField(blank=True, null=True)
    client_login_id = models.ForeignKey(User, models.DO_NOTHING)
    cond_id = models.SmallIntegerField(blank=True, null=True)
    airconds_count = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'client_airconddata'
