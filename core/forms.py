
from django.forms import ModelForm
from django import forms
from . models import ExerciseTrainingUnit, MainExercise, Exercise, TrainingPlan, MainUserProfile, TrainingUnit
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
        fields =['user','nameoftheplan','mesocycle','timeoftheplan','Benchpress1RM','DeadliftT1RM','Squat1RM',]
        # widgets= {
        # 'user': forms.TextInput(attrs={'class':'form-control','value':'','id':'melder','type':'hidden'}), }


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
        fields=['exercisename','exercisesets','exercisereps']

        widgets= {
        'trainingplan': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'',
        }),
        }


        model = ExerciseTrainingUnit
        fields=['exercisename','exercisesets','exercisereps']
        widgets= {
        'trainingunit': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'',
        }),}

class TrainingUnitForm(ModelForm):
    class Meta:

        model = TrainingUnit
        fields=['trainingplan']

        widgets= {
        'trainingplan': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'',
        }),
        }