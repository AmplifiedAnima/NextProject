# Generated by Django 4.1.1 on 2022-10-28 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_trainingplan_user_remove_trainingplan_exercises_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingplan',
            name='Exercises',
        ),
        migrations.AddField(
            model_name='trainingplan',
            name='Exercises',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.exercise'),
            preserve_default=False,
        ),
    ]
