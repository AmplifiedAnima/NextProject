from django.urls import path
from . import views 


urlpatterns = [
path ('', views.HomePage, name="homepage"),
path ('homepage/', views.HomePage, name="homepage"),

path('login/', views.logpage, name="login"),
path('logout/', views.logoutUser, name="logout"),
path('register/', views.registerPage, name="register"),
path ('profilepage/', views.ProfilePage, name="profilepage"),

path ('trainingplan/<str:pk>/',views.TrainingPlanForUser, name="trainingplan"),
path ('trainingunit/<str:pk>/',views.TrainingUnitInPlan, name="trainingunit"),
path ('renderpdf/<str:pk>', views.render_pdf_view, name="renderpdf"),
path ('addtrainingplan',views.AddTrainingPlan, name="addtrainingplan"),

path ('trainingunitfreelance/<str:pk>/',views.TrainingUnitInPlanFreelance, name="trainingunitfreelance"),
path ('trainingplanfreelance/<str:pk>/',views.TrainingPlanFreelance, name="trainingplanfreelance"),
path ('renderpdfnotperiodized/<str:pk>', views.render_pdf_view_nonperiodized, name="renderpdfnotperiodized"), 
path ('addtrainingfreelance',views.AddTrainingPlanFreelance, name="addtrainingfreelance"),



]