from django.contrib import admin

from core.models import MainExercise, Exercise, MainUserProfile, TrainingPlan, TrainingUnit, ExerciseTrainingUnit
# Register your models here.
admin.site.register(Exercise)
admin.site.register(MainExercise)
# admin.site.register(TrainingUnit)
admin.site.register(TrainingPlan)
admin.site.register(TrainingUnit)
admin.site.register(MainUserProfile)
admin.site.register(ExerciseTrainingUnit)