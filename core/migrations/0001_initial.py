# Generated by Django 4.1.1 on 2022-10-27 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercisename', models.CharField(max_length=100, verbose_name='Exercise')),
                ('exercisesets', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], max_length=20)),
                ('exercisereps', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Squat1RM', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='100% maximal repetition in squat')),
                ('DeadliftT1RM', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='100% maximal repetition in deadlift')),
                ('Benchpress1RM', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='100% maximal repetition in benchpress')),
                ('mesocycle', models.CharField(choices=[('GPP', 'GPP'), ('ACC', 'ACC'), ('PEAK', 'PEAK'), ('CASUALTRAINING', 'CASUALTRAINING')], default='GPP', max_length=20)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accesoryexercises', models.ManyToManyField(to='core.exercise')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MainUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('from_signal', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
