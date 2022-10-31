
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import MainUserProfile, TrainingPlan,TrainingUnit, ExerciseTrainingUnit

@receiver(post_save, sender=User)
def post_save_create_user(sender, instance, created, **kwargs):
    if created:
        MainUserProfile.objects.create(user=instance)
       
@receiver(post_save, sender=TrainingPlan)
def post_save_create_trainingunits(sender,instance,created,**kwargs):
    if created:
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)
        TrainingUnit.objects.create(trainingplan=instance)


@receiver(post_save, sender=TrainingUnit)
def post_save_create_exercises(sender,instance,created,**kwargs):
    if created:
        ExerciseTrainingUnit.objects.create(trainingunit=instance)
        ExerciseTrainingUnit.objects.create(trainingunit=instance)
        ExerciseTrainingUnit.objects.create(trainingunit=instance)

