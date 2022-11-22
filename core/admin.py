from django.contrib import admin

from core.models import MainExercise,NewbieExercise,NewbieTrainingPlan,NewbieTrainingUnit, Exercise, MainUserProfile, TrainingPlan, TrainingUnit
# Register your models here.
admin.site.register(Exercise)
admin.site.register(NewbieExercise)
admin.site.register(MainExercise)
# admin.site.register(TrainingUnit)
admin.site.register(TrainingPlan)
admin.site.register(NewbieTrainingPlan)
admin.site.register(TrainingUnit)
admin.site.register(NewbieTrainingUnit)
admin.site.register(MainUserProfile)
