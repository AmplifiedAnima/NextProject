# Generated by Django 4.1.1 on 2022-10-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_mainexercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainexercise',
            name='maximalrepetition',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Your 1RM for given exercise'),
        ),
    ]
