# Generated by Django 4.1.1 on 2022-10-31 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_exercisetrainingunit'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisetrainingunit',
            name='from_signal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trainingplan',
            name='from_signal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trainingunit',
            name='from_signal',
            field=models.BooleanField(default=False),
        ),
    ]
