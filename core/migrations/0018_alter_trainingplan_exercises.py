# Generated by Django 4.1.1 on 2022-10-28 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_trainingplan_exercises_trainingplan_exercises'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingplan',
            name='Exercises',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.exercise'),
        ),
    ]