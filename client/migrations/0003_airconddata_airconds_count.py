# Generated by Django 4.0.3 on 2022-03-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_airconddata_cond_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='airconddata',
            name='airconds_count',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
