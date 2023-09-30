# Generated by Django 4.2.5 on 2023-09-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='address',
            field=models.CharField(default='Address', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointment_title',
            field=models.CharField(default='Appt Title', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.CharField(default='date', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor_name',
            field=models.CharField(default='Doctor Name', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor_specialist',
            field=models.CharField(default='Doctor Specialist', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='notes',
            field=models.CharField(default='Notes', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.CharField(default='Time', max_length=200),
            preserve_default=False,
        ),
    ]
