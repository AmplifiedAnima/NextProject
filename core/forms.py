
from django.forms import ModelForm
from django import forms
from . models import MainExercise,NewbieExercise, Exercise, TrainingPlan, MainUserProfile, TrainingUnit,NewbieTrainingUnit, NewbieTrainingPlan
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

class NewbieTrainingForm(ModelForm):
    class Meta:
        model = NewbieTrainingPlan
        fields= fields =['user','nameoftheplan','timeoftheplan']
        widgets= {
        'user': forms.TextInput(attrs={'class':'form-control','value':'','id':'melder','type':'hidden'}), 
        }

        #'Benchpress1RM','DeadliftT1RM','Squat1RM',

class MainExerciseForm(ModelForm):
    class Meta:

        model = MainExercise
        fields=['mainexercise','exercisereps','exercisesets','trainingunit','intensity']

        widgets= {
        'trainingunit': forms.TextInput(attrs={'class':'form-control','value':'','id':'welder','type':'hidden',}),
        'intensity': forms.TextInput(attrs={'class':'form-control','value':'100','id':'','type':'',
        }),
        }

        
class TrainingUnitForm(ModelForm):
    class Meta:
        model = TrainingUnit
        fields=['name','trainingplan']

        widgets= {
        'trainingplan': forms.TextInput(attrs={'class':'form-control','value':'','id':'tren','type':'',
        }),
        }   

class NewbieTrainingUnitForm(ModelForm):
    class Meta:
        model = NewbieTrainingUnit
        fields=['name','trainingplan']

        widgets= {
        'trainingplan': forms.TextInput(attrs={'class':'form-control','value':'','id':'tren','type':'hidden',
        }),
        'name': forms.TextInput(attrs={'class':'form-control','value':'Training unit','id':'','type':'',
           }),}   

class ExerciseForm(ModelForm):
    class Meta:

        model = Exercise
        fields=['exercisename','exercisesets','exercisereps','trainingunit']
        widgets= {
        'trainingunit': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden',
        }),}


class NewbieExerciseForm(ModelForm):
    class Meta:
        model = NewbieExercise
        fields=['exercisename','exercisesets','exercisereps','trainingunit']
        widgets= {
        'trainingunit': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden',
        }),}



