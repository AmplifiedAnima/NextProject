# Generated by Django 4.1.1 on 2022-10-29 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_trainingplan_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='exercisename',
            field=models.CharField(choices=[('Overhead Press - bilateral', 'Overhead Press- bilateral'), ('Overhead Press - unilateral', 'Overhead Press -unilateral'), ('Windmill', 'Windmill'), ('Rows', 'Rows'), ('Overhead Press - bilateral', 'Overhead Press'), ('Bent press', 'Bent press')], max_length=100, verbose_name='Exercise'),
        ),
    ]
