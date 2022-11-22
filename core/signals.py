import random
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import MAIN_EXERCISE_CHOICES, MESOCYCLE_GPP, MESOCYCLE_ACC,MESOCYCLE_PEAK, LOWERBODY_UNILATERAL_CHOICES,LOWEBODY_BILATERAL_CHOICES,UPPERBODY_UNILATERAL_CHOICES,UPPERBODY_BILATERAL_CHOICES, TIME_WEEK2,TIME_WEEK3,TIME_WEEK4,MainExercise,Exercise, MainUserProfile,NewbieTrainingPlan, TrainingPlan,NewbieTrainingUnit,TrainingUnit,NewbieExercise

@receiver(post_save, sender=User)
def post_save_create_user(sender, instance, created, **kwargs):
    if created:
        MainUserProfile.objects.create(user=instance)
       
@receiver(post_save, sender=TrainingPlan)
def post_save_create_trainingunits(sender,instance, created,**kwargs):

    if created:
     
        if instance.mesocycle==MESOCYCLE_GPP or instance.mesocycle==MESOCYCLE_PEAK:

            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day I')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day II')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day III')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day IV')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day V')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day VI')
         

        if instance.mesocycle==MESOCYCLE_ACC:
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day I')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day II')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day III')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day IV')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day V')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day VI')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day VII')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day VIII')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day IX')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day X')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day XI')
            TrainingUnit.objects.create(trainingplan=instance, name='Training unit day XII')
                

@receiver(post_save, sender=TrainingUnit)
def post_save_create_exercises(sender,instance,created,**kwargs):
    if created:
        Exercise.objects.create(exercisename=random.choices(UPPERBODY_BILATERAL_CHOICES)[0][0],exercisesets=2,exercisereps=10,trainingunit=instance)
        Exercise.objects.create(exercisename=random.choices(UPPERBODY_UNILATERAL_CHOICES)[0][0],exercisesets=2,exercisereps=10,trainingunit=instance)
        Exercise.objects.create(exercisename=random.choices(LOWERBODY_UNILATERAL_CHOICES)[0][0],exercisesets=2,exercisereps=10,trainingunit=instance)




@receiver(post_save, sender=NewbieTrainingPlan)
def post_save_create_newbietrainingunits(sender,instance,created,**kwargs):
    if created:
        if instance.timeoftheplan== TIME_WEEK2:

            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit unit day I')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day II')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day III')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day IV')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day V')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day VI')

        if instance.timeoftheplan== TIME_WEEK3:  

            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day I')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day II')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day III')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day IV')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day V')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day VI')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day VII')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day VIII')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day IX')

        if instance.timeoftheplan== TIME_WEEK4: 

            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day I')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day II')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day III')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day IV')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day V')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day VI')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day VII')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day VIII')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day IX')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day X')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day XI')
            NewbieTrainingUnit.objects.create(trainingplan=instance, name='Training unit day XII')


@receiver(post_save, sender=NewbieTrainingUnit)
def post_save_create_newbieexercises(sender,instance,created,**kwargs):
    if created:
        NewbieExercise.objects.create(exercisename=random.choices(UPPERBODY_BILATERAL_CHOICES)[0][0],exercisesets=2,exercisereps=10,trainingunit=instance)
        NewbieExercise.objects.create(exercisename=random.choices(UPPERBODY_UNILATERAL_CHOICES)[0][0],exercisesets=2,exercisereps=10,trainingunit=instance)
        NewbieExercise.objects.create(exercisename=random.choices(LOWERBODY_UNILATERAL_CHOICES)[0][0],exercisesets=2,exercisereps=10,trainingunit=instance)


# EXERCISE_CHOICES=[
#     (OVERHEADPRESS, "Overhead Press - bilateral"),
#     (OVERHEADPRESSU, "Overhead Press - unilateral"),
#     (WINDMILL, "Windmill"),
#     (ROWS,"Rows"),
#     (OVERHEADPRESS,"Overhead Press"),
#     (BENTPRESS, "Bent press"),
#     (BILATERALSWING, "Bilateral Swing"),
#     (UNILATERALSWING,"Unilateral Swing"),
#     (SNATCH , "Snatch"),
#     (SQUAT , "Squat"),
#     (LUNGES , "Lunges"),
#     (LUNGES,"Lunges"),
#     (BACKWARDLUNGES, "Backward Lunges"),
#     (HACKSQUAT ,"Hacksquat"),
#     (ROMAINIANDL,"ROMAINIANDL"),
#     (ONESIDELEGDL,"Unilateral Romainian Deadlift"),
#     (CLASSICDEADLIFT,"Classic Deadlift"),
# ]