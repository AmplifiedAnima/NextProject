# Generated by Django 4.1.1 on 2022-10-27 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_trainingplan_timeoftheplan_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingplan',
            name='trainingunits',
        ),
        migrations.AddField(
            model_name='trainingplan',
            name='Exercises',
            field=models.ManyToManyField(to='core.exercise'),
        ),
        migrations.DeleteModel(
            name='TrainingUnit',
        ),
    ]
