# Generated by Django 4.1.1 on 2022-10-30 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_remove_trainingplan_benchpress1rm_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainexercise',
            name='trainingunit',
        ),
        migrations.AddField(
            model_name='mainexercise',
            name='trainingplan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.trainingplan'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mainexercise',
            name='maximalrepetition',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Your 1RM for given exercise in kg'),
        ),
    ]
