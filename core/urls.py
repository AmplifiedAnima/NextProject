from django.urls import path
from . import views


urlpatterns = [
path ('', views.HomePage, name="homepage"),
path ('homepage/', views.HomePage, name="homepage"),
path ('trainingplan/<str:pk>/',views.TrainingPlanForUser, name="trainingplan"),
# path ('trainingplansecond/<str:pk>/',views.TrainingPlanForUserNew, name="trainingplansecond"),
path ('addtrainingplan',views.AddTrainingPlan, name="addtrainingplan"),
]