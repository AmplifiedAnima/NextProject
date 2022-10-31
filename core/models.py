from random import choices
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class MainUserProfile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=30)
    email = models.EmailField(max_length=200, null=True)
    image= models.ImageField(null=True, blank=True,upload_to="images/profile/")
    from_signal = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)


     
BENTPRESS="Bent press"
WINDMILL="Windmill"
ROWS="Rows"
OVERHEADPRESS="Overhead Press - bilateral"
OVERHEADPRESSU="Overhead Press - unilateral"
EXERCISE_CHOICES=[
    (OVERHEADPRESS, "Overhead Press - bilateral"),
    (OVERHEADPRESSU, "Overhead Press - unilateral"),
    (WINDMILL, "Windmill"),
    (ROWS,"Rows"),
    (OVERHEADPRESS,"Overhead Press"),
    (BENTPRESS, "Bent press"),]







# class TrainingUnit(models.Model):
#     name= models.CharField(max_length=20,blank=True,null=True)
#     Exercises=models.ManyToManyField(Exercise)
#     updated = models.DateTimeField(auto_now=True)
#     created= models.DateTimeField(auto_now_add=True)


#     def __str__(self):
#         return str(self.name)



        
MESOCYCLE_GPP= "General physical preparation phase"
MESOCYCLE_ACC= "Acumulation phase"
MESOCYCLE_PEAK= "Peak phase"
MESOCYCLE_CASUALTRAINING= "Casual Training"
MESOCYCLE_NONE="None"
MESOCYCLE_CHOICES=[
    (MESOCYCLE_GPP, "GPP"),
    (MESOCYCLE_ACC, "ACC"),
    (MESOCYCLE_PEAK, "PEAK"),
    (MESOCYCLE_CASUALTRAINING, "Casual training"),
    (MESOCYCLE_NONE,"None")]


TIME_WEEK2="2 Weeks"
TIME_WEEK3="3 Weeks"
TIME_WEEK4="4 Weeks"
TIME_CHOICE=[
    (TIME_WEEK2, "2 Weeks"),
    (TIME_WEEK3, "3 Weeks"),
    (TIME_WEEK4, "4 Weeks"),]


SQUAT= "Squat"
DEADLIFT= "Deadlift"
BENCHPRESS= "Benchpress"
MAIN_EXERCISE_CHOICES=[
    (SQUAT, "Squat"),
    (DEADLIFT, "Deadlift"),
    (BENCHPRESS, "Benchpress")]

class TrainingPlan(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    nameoftheplan = models.CharField(verbose_name="Name of the plan",max_length=20, null=True)
    Squat1RM = models.PositiveIntegerField(verbose_name="100%RM in squat",default=0, blank=True, null=True)
    DeadliftT1RM =models.PositiveIntegerField(verbose_name="100%RM maximal repetition in deadlift",default=0, blank=True, null=True)
    Benchpress1RM = models.PositiveIntegerField(verbose_name="100%RM maximal repetition in benchpress",default=0, blank=True, null=True)
    mesocycle= models.CharField(max_length=40, choices=MESOCYCLE_CHOICES,default=MESOCYCLE_GPP)
    timeoftheplan= models.CharField(max_length=40,choices=TIME_CHOICE,default=TIME_WEEK3 )
    from_signal = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.nameoftheplan)


class TrainingUnit(models.Model):
    trainingplan=models.ForeignKey(TrainingPlan, on_delete=models.CASCADE)
    from_signal = models.BooleanField(default=False)
    

SETSCHOICES=[(i,i)for i in range(5)]
AMRAP="AMRAP"
REPCHOICES= [(i,i)for i in range(20)]
              

class ExerciseTrainingUnit(models.Model):
    trainingunit=models.ForeignKey(TrainingUnit, on_delete=models.CASCADE)
    exercisename=models.CharField(max_length=100,verbose_name="Exercise",choices=EXERCISE_CHOICES)
    exercisesets=models.IntegerField(choices=SETSCHOICES,default=1)
    exercisereps=models.IntegerField(choices=REPCHOICES,default=1)
    from_signal = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.exercisename)

class MainExercise(models.Model):
    mainexercise= models.CharField(max_length=100,verbose_name="Main Exercise",choices=MAIN_EXERCISE_CHOICES)
    maximalrepetition = models.IntegerField(verbose_name="Your 1RM for given exercise in kg",default=0,blank=True,null=True)
    trainingplan= models.ForeignKey(TrainingPlan, on_delete=models.CASCADE)

    def __str__(self):
        return self.mainexercise

class Exercise(models.Model):
    trainingplan=models.ForeignKey(TrainingPlan,on_delete=models.CASCADE)
    exercisename=models.CharField(max_length=100,verbose_name="Exercise",choices=EXERCISE_CHOICES)
    exercisesets=models.IntegerField(choices=SETSCHOICES,default=1)
    exercisereps=models.IntegerField(choices=REPCHOICES,default=1)
    
    def __str__(self):
        return str(self.exercisename)





