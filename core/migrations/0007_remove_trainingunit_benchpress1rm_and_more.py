# Generated by Django 4.1.1 on 2022-10-27 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_trainingplan_nameoftheplan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingunit',
            name='Benchpress1RM',
        ),
        migrations.RemoveField(
            model_name='trainingunit',
            name='DeadliftT1RM',
        ),
        migrations.RemoveField(
            model_name='trainingunit',
            name='Squat1RM',
        ),
        migrations.RemoveField(
            model_name='trainingunit',
            name='mesocycle',
        ),
        migrations.RemoveField(
            model_name='trainingunit',
            name='name',
        ),
        migrations.AddField(
            model_name='trainingplan',
            name='Benchpress1RM',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='100% maximal repetition in benchpress'),
        ),
        migrations.AddField(
            model_name='trainingplan',
            name='DeadliftT1RM',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='100% maximal repetition in deadlift'),
        ),
        migrations.AddField(
            model_name='trainingplan',
            name='Squat1RM',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='100% maximal repetition in squat'),
        ),
        migrations.AddField(
            model_name='trainingplan',
            name='mesocycle',
            field=models.CharField(choices=[('GPP', 'GPP'), ('ACC', 'ACC'), ('PEAK', 'PEAK'), ('Casual Training', 'Casual training'), ('NONE', 'Mesocycle - none')], default='GPP', max_length=20),
        ),
        migrations.AlterField(
            model_name='trainingplan',
            name='nameoftheplan',
            field=models.CharField(max_length=20, null=True, verbose_name='Name of the plan'),
        ),
        migrations.RemoveField(
            model_name='trainingplan',
            name='trainingunits',
        ),
        migrations.AddField(
            model_name='trainingplan',
            name='trainingunits',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.trainingunit'),
        ),
    ]
