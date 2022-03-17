# Generated by Django 4.0.3 on 2022-03-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_rename_client_login_airconddata_client_login_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAirconddata',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('t1', models.SmallIntegerField(blank=True, null=True)),
                ('t2', models.SmallIntegerField(blank=True, null=True)),
                ('t3', models.SmallIntegerField(blank=True, null=True)),
                ('t4', models.SmallIntegerField(blank=True, null=True)),
                ('t5', models.SmallIntegerField(blank=True, null=True)),
                ('pressure', models.SmallIntegerField(blank=True, null=True)),
                ('current', models.SmallIntegerField(blank=True, null=True)),
                ('cond_id', models.SmallIntegerField(blank=True, null=True)),
                ('airconds_count', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'client_airconddata',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='AircondData',
        ),
    ]