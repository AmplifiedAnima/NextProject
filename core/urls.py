from django.urls import path
from . import views


urlpatterns = [
path ('', views.HomePage, name="homepage"),
path ('homepage/', views.HomePage, name="homepage"),
path ('trainingplan/<str:pk>/',views.TrainingPlanForUser, name="trainingplan"),
path ('trainingunit/<str:pk>/',views.TrainingUnitInPlan, name="trainingunit"),
path ('trainingplanfreelance<str:pk>/',views.TrainingPlanFreelance, name="trainingplanfreelance"),
path ('addtrainingplan',views.AddTrainingPlan, name="addtrainingplan"),
path ('addtrainingplanfreelance',views.AddTrainingPlanFreelance, name="addtrainingplanfreelance"),
]