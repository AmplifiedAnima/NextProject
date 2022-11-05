
from django.forms import ModelForm
from django import forms
from . models import MainExercise, Exercise, TrainingPlan, MainUserProfile, TrainingUnit, NewbieTrainingPlan
from django.contrib.auth.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields =['username','email']
        
    
class ChangeProfile(ModelForm):
    class Meta:
        model = MainUserProfile
        fields='__all__'

class TrainingForm(ModelForm):
    class Meta:
        model = TrainingPlan
        fields =['user','nameoftheplan','mesocycle','Benchpress1RM','DeadliftT1RM','Squat1RM',]
        widgets= {
        'user': forms.TextInput(attrs={'class':'form-control','value':'','id':'melder','type':'hidden'}), }

        model = NewbieTrainingPlan
        fields= fields =['user','nameoftheplan']
        widgets= {
        'user': forms.TextInput(attrs={'class':'form-control','value':'','id':'melder','type':'hidden'}), }

        #'Benchpress1RM','DeadliftT1RM','Squat1RM',

class MainExerciseForm(ModelForm):
    class Meta:

        model = MainExercise
        fields='__all__'

        widgets= {
        'trainingplan': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'',
        }),
        }

class ExerciseForm(ModelForm):
    class Meta:

        model = Exercise
        fields=['exercisename','exercisesets','exercisereps','trainingunit']
        widgets= {
        'trainingunit': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden',
        }),}

class TrainingUnitForm(ModelForm):
    class Meta:
        model = TrainingUnit
        fields=['name','trainingplan']

        widgets= {
        'trainingplan': forms.TextInput(attrs={'class':'form-control','value':'','id':'tren','type':'',
        }),
        }   