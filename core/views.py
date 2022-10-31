from pickle import NONE
from django.contrib import messages
from django.shortcuts import render,redirect
from core.forms import ExerciseForm, TrainingForm,TrainingUnitForm

from core.models import MainExercise, TrainingPlan,Exercise, TrainingUnit,MAIN_EXERCISE_CHOICES
# Create your views here.


def HomePage(request):
    treningi = TrainingPlan.objects.all()
    context = {'treningi': treningi}
    return render(request, 'core/homepage.html',context)

trainingplans=[]
exercises=()

def TrainingPlanForUser(request,pk):
    exercise=''
    training = TrainingPlan.objects.get(id=pk)
    SQUAT1RM = TrainingPlan.objects.values('Squat1RM').get(id=pk)
    DEADLIFT1RM = TrainingPlan.objects.values('DeadliftT1RM').get(id=pk)
    BENCHPRESS1RM= TrainingPlan.objects.values('Benchpress1RM').get(id=pk)
      
    sq=SQUAT1RM.get('Squat1RM')
    dl=DEADLIFT1RM.get('DeadliftT1RM')
    bp=BENCHPRESS1RM.get('Benchpress1RM')

    mezocykl=TrainingPlan.objects.values('mesocycle').get(id=pk)
    mesocycle= mezocykl.get('mesocycle')

   #CASUALTRAINING
    gppsets1=[2,3]
    gppsets2=[3,4]
    gpprepsrange1=[16,24]
    gpprepsrange2=[16,30]
    #GENERAL PHYSICAL PREPRATION SETS AND REP RANGES and Cas
    gppsets1=[2,3]
    gppsets2=[3,4]
    gpprepsrange1=[16,24]
    gpprepsrange2=[16,30]
    gppsq1w=[round(sq*0.70),round(sq*0.72,5),round(sq*0.75) ]
    gppsq2w=[round(sq*0.72,5),round(sq*0.75),round(sq*0.77,5)]
    gppdl1w=[round(dl*0.70),round(dl*0.72,5),round(dl*0.75)]
    gppdl2w=[round(dl*0.72,5),round(dl*0.75),round(dl*0.77,5)]
    gppbp1w=[round(bp*0.70),round(bp*0.72,5),round(bp*0.75)]
    gppbp2w=[round(bp*0.72,5),round(bp*0.75),round(bp*0.77,5)]
    #ACCUMULATION PHASE SETS AND REP RANGES +(INTENSITY= PIREPLIN'S TABLE)
    accrepsrange1=[18,30]
    accrepsrange2=[12,24]
    accrepsrange3=[10,20]
    accrepsrange4=[10,18]
    accsets1=[3,6]
    accsets2=[3,6]
    accsets3=[2,4]
    accsets4=[2,3]
    accsq1w= [round(sq*0.55),round(sq*0.57,5), round(sq*0.60), round(sq*0.62,5), round(sq*0.65)]
    accsq2w= [round(sq*0.67,5),round(sq*0.70),round(sq*0.72,5),round(sq*0.75),round(sq*0.77,5)]
    accsq3w= [round(sq*0.8),round(sq*0.82,5),round(sq*0.85),round(sq*0.87,5),round(sq*0.9)]
    accsq4w= [round(sq*0.5),round(sq*0.52,5),round(sq*0.55),round(sq*0.6)]
    accdl1w= [round(dl*0.55),round(dl*0.57,5), round(dl*0.60), round(dl*0.62,5), round(dl*0.65)]
    accdl2w= [round(dl*0.67,5),round(dl*0.70),round(dl*0.72,5),round(dl*0.75),round(dl*0.77,5)]
    accdl3w= [round(dl*0.8),round(dl*0.82,5),round(dl*0.85),round(dl*0.87,5),round(dl*0.9)]
    accdl4w= [round(dl*0.5),round(dl*0.52,5),round(dl*0.55),round(dl*0.6)]
    accbp1w= [round(bp*0.55),round(bp*0.57,5), round(bp*0.60), round(bp*0.62,5), round(bp*0.65)]
    accbp2w= [round(bp*0.67,5),round(bp*0.70),round(bp*0.72,5),round(bp*0.75),round(bp*0.77,5)]
    accbp3w= [round(bp*0.8),round(bp*0.82,5),round(bp*0.85),round(bp*0.87,5),round(bp*0.9)]
    accbp4w= [round(bp*0.5),round(bp*0.52,5),round(bp*0.55),round(bp*0.6)]
    #PEAK
    peakrepsrange1=[8,10]
    peakrepsrange2=[5,8]
   
    peaksets1=[5,8]
    peaksets2=[3,5]
    peaksets3=('PEAK', 'MAX OUT!')
    peaksets4=('Rest...', 'Start from gpp again')
    
    peaksq1w= [round(sq*0.87,5),round(sq*0.9),round(sq*0.92,5), round(sq*0.95) ]
    peaksq2w= [round(sq*0.90),round(sq*0.92,5),round(sq*0.95)]
    peakdl1w= [round(dl*0.87,5),round(dl*0.9),round(dl*0.92,5), round(dl*0.95)]
    peakdl2w= [round(dl*0.90),round(dl*0.92,5),round(dl*0.95)]
    peakbp1w= [round(bp*0.87,5),round(bp*0.9),round(bp*0.92,5), round(bp*0.95)]
    peakbp2w= [round(bp*0.90),round(bp*0.92,5),round(bp*0.95)]


    
    if training.mesocycle == "Casual training" or "GPP":
        a= (f'{gppsets1[0]} - {gppsets1[1]}'),(f'{gpprepsrange1[0]} - {gpprepsrange1[1]}'),(f'{gppsq1w[0]}kg, {gppsq1w[1]}kg, {gppsq1w[2]}kg')
        a1=(f'{gppsets1[0]} - {gppsets1[1]}'),(f'{gpprepsrange1[0]} - {gpprepsrange1[1]}'),(f'{gppdl1w[0]}kg, {gppdl1w[1]}kg, {gppdl1w[2]}kg')
        a2=(f'{gppsets1[0]} - {gppsets1[1]}'),(f'{gpprepsrange1[0]} - {gpprepsrange1[1]}'),(f'{gppbp1w[0]}kg, {gppbp1w[1]}kg, {gppbp1w[2]}kg')
        b= (f'{gppsets2[0]} - {gppsets2[1]}'),(f'{gpprepsrange2[0]} - {gpprepsrange2[1]}'),(f'{gppsq2w[0]}kg, {gppsq2w[1]}kg, {gppsq2w[2]}kg')
        b1=(f'{gppsets2[0]} - {gppsets2[1]}'),(f'{gpprepsrange2[0]} - {gpprepsrange2[1]}'),(f'{gppdl2w[0]}kg, {gppdl2w[1]}kg, {gppdl2w[2]}kg')
        b2=(f'{gppsets2[0]} - {gppsets2[1]}'),(f'{gpprepsrange2[0]} - {gpprepsrange2[1]}'),(f'{gppbp2w[0]}kg, {gppbp2w[1]}kg, {gppbp2w[2]}kg')
        c= f''
        c1=f''
        c2=f''
        d= f''
        d1=f''
        d2=f''

    
    if training.mesocycle == "Acumulation phase":
        a= (f'{accsets1[0]} - {accsets1[1]}'),(f'{accrepsrange1[0]} - {accrepsrange1[1]}'),(f'{accsq1w[0]}kg, {accsq1w[1]}kg, {accsq1w[2]}kg, {accsq1w[3]}kg, {accsq1w[4]}kg')
        a1=(f'{accsets1[0]} - {accsets1[1]}'),(f'{accrepsrange1[0]} - {accrepsrange1[1]}'),(f'{accdl1w[0]}kg, {accdl1w[1]}kg, {accdl1w[2]}kg, {accdl1w[3]}kg, {accdl1w[4]}kg')
        a2=(f'{accsets1[0]} - {accsets1[1]}'),(f'{accrepsrange1[0]} - {accrepsrange1[1]}'),(f'{accbp1w[0]}kg, {accbp1w[1]}kg, {accbp1w[2]}kg, {accbp1w[3]}kg, {accbp1w[4]}kg ')
        b= (f'{accsets2[0]} - {accsets2[1]}'),(f'{accrepsrange2[0]} - {accrepsrange2[1]}'),(f'{accsq2w[0]}kg, {accsq2w[1]}kg, {accsq2w[2]}kg, {accsq2w[3]}kg, {accsq2w[4]}kg')
        b1=(f'{accsets2[0]} - {accsets2[1]}'),(f'{accrepsrange2[0]} - {accrepsrange2[1]}'),(f'{accdl2w[0]}kg, {accdl2w[1]}kg, {accdl2w[2]}kg, {accdl2w[3]}kg, {accdl2w[4]}kg')
        b2=(f'{accsets2[0]} - {accsets2[1]}'),(f'{accrepsrange2[0]} - {accrepsrange2[1]}'),(f'{accbp2w[0]}kg, {accbp2w[1]}kg, {accbp2w[2]}kg, {accbp2w[3]}kg, {accbp2w[4]}kg')
        c= (f'{accsets3[0]} - {accsets3[1]}'),(f'{accrepsrange3[0]} - {accrepsrange3[1]}'),(f'{accsq3w[0]}kg, {accsq3w[1]}kg, {accsq3w[2]}kg, {accsq3w[3]}kg, {accsq3w[4]}kg')
        c1=(f'{accsets3[0]} - {accsets3[1]}'),(f'{accrepsrange3[0]} - {accrepsrange3[1]}'),(f'{accdl3w[0]}kg, {accdl3w[1]}kg, {accdl3w[2]}kg, {accdl3w[3]}kg, {accdl3w[4]}kg')
        c2=(f'{accsets3[0]} - {accsets3[1]}'),(f'{accrepsrange3[0]} - {accrepsrange3[1]}'),(f'{accbp3w[0]}kg, {accbp3w[1]}kg, {accbp3w[2]}kg, {accbp3w[3]}kg, {accbp3w[4]}kg')
        d= (f'{accsets4[0]} - {accsets4[1]}'),(f'{accrepsrange4[0]} - {accrepsrange4[1]}'),(f'{accsq4w[0]}kg, {accsq4w[1]}kg, {accsq4w[2]}kg, {accsq4w[3]}kg')
        d1=(f'{accsets4[0]} - {accsets4[1]}'),(f'{accrepsrange4[0]} - {accrepsrange4[1]}'),(f'{accdl4w[0]}kg, {accdl4w[1]}kg, {accdl4w[2]}kg, {accdl4w[3]}kg')
        d2=(f'{accsets4[0]} - {accsets4[1]}'),(f'{accrepsrange4[0]} - {accrepsrange4[1]}'),(f'{accbp4w[0]}kg, {accbp4w[1]}kg, {accbp4w[2]}kg, {accbp4w[3]}kg')


    if training.mesocycle == "Peak phase":
        a= (f'{peaksets1[0]} - {peaksets1[1]}'),(f'{peakrepsrange1[0]} - {peakrepsrange1[1]}'),(f'{peaksq1w[0]}kg, {peaksq1w[1]}kg, {peaksq1w[2]}kg,  {peaksq1w[3]}kg')
        a1=(f'{peaksets1[0]} - {peaksets1[1]}'),(f'{peakrepsrange1[0]} - {peakrepsrange1[1]}'),(f'{peakdl1w[0]}kg, {peakdl1w[1]}kg, {peakdl1w[2]}kg,  {peakdl1w[2]}kg')
        a2=(f'{peaksets1[0]} - {peaksets1[1]}'),(f'{peakrepsrange1[0]} - {peakrepsrange1[1]}'),(f'{peakbp1w[0]}kg, {peakbp1w[1]}kg, {peakbp1w[2]}kg,  {peakbp1w[2]}kg')
        b= (f'{peaksets2[0]} - {peaksets2[1]}'),(f'{peakrepsrange2[0]} - {peakrepsrange2[1]}'),(f'{peaksq2w[0]}kg, {peaksq2w[1]}kg, {peaksq2w[2]}kg')
        b1=(f'{peaksets2[0]} - {peaksets2[1]}'),(f'{peakrepsrange2[0]} - {peakrepsrange2[1]}'),(f'{peakdl2w[0]}kg, {peakdl2w[1]}kg, {peakdl2w[2]}kg')
        b2=(f'{peaksets2[0]} - {peaksets2[1]}'),(f'{peakrepsrange2[0]} - {peakrepsrange2[1]}'),(f'{peakbp2w[0]}kg, {peakbp2w[1]}kg, {peakbp2w[2]}kg')
        c=(str(peaksets3[0]),"",str(peaksets3[0]))
        c1=(str(peaksets3[0]),"",str(peaksets3[1]))
        c2=(str(peaksets3[0]),"",str(peaksets3[0]))
        d= ()
        d1=()
        d2=str(peaksets4[0]),"",str(peaksets4[1])

    exercises = training.exercise_set.all()
    trainingunits=training.trainingunit_set.all()
    # trainingunitexercises=training.exercisetrainingunit_set.all()
    day1=trainingunits[0]
    day2=trainingunits[1]
    day3=trainingunits[2]
    day4=trainingunits[3]
    day5=trainingunits[4]
    day6=trainingunits[5]
    day7=trainingunits[6]
    day8=trainingunits[7]
    day9=trainingunits[8]
    day10=trainingunits[9]
    day11=trainingunits[10]
    day12=trainingunits[11]
    

    


    




    if request.method =="POST":
        exercise = ExerciseForm(request.POST)
        if exercise.is_valid():
            exercise=Exercise.objects.create(
            trainingplan=TrainingPlan.objects.get(id=pk),
            exercisename=request.POST.get('exercisename'),
            exercisesets=request.POST.get('exercisesets'),
            exercisereps=request.POST.get('exercisereps'),
            )


    # if request.method =="POST":
    #     exercise = TrainingUnitForm(request.POST)
    #     if exercise.is_valid():
    #         exercise=Exercise.objects.create(
    #         trainingplan=TrainingPlan.objects.get(id=pk),
    #         exercisename=request.POST.get('exercisename'),
    #         exercisesets=request.POST.get('exercisesets'),
    #         exercisereps=request.POST.get('exercisereps'),
    #         )


    
        
    context={ 'a':a,'a1':a1,'a2':a2 ,'b':b,'b1':b1,'b2':b2, 'c':c,'c1':c1,
    'c2':c2, 'd':d, 'd1':d1,'d2':d2 ,'sq':sq,'dl':dl,'bp':bp, 'exercises':exercises ,
    'training': training,
    'mesocycle': mesocycle,
    'training.mesocycle': training.mesocycle,'exercise':exercise,'trainingunits':trainingunits,
    'day1':day1 ,'day2':day2,'day3':day3,'day4':day4,'day5':day5,'day6':day6,
    'day7':day7,'day8':day8,'day9':day9,'day10':day10,'day11':day11,'day12':day12}
    return render(request, 'core/trainingplan.html',context)


def AddTrainingPlan(request):
    training = TrainingForm()

    if request.method =="POST":
        training = TrainingForm(request.POST)
        if training.is_valid():
            trainingplans.append(training)
            training.user=request.user
            training.save()
            return redirect('homepage')
        context= {'training': training}

        return render(request,'core/addtrainingplan.html', context)
    else:
        return render(request, 'core/addtrainingplan.html', {"training": training})   





# def TrainingPlanForUserNew(request,pk):
    
#     main1=''
#     main2=''
#     main3=''
#     main4=''
#     training = TrainingPlan.objects.get(id=pk)
#     mainexercises =training.mainexercise_set.all()
#     mainexercises1 =training.mainexercise_set.all()
#     trainingun= training.trainingunit_set.all()

#     # if len(mainexercises)<=3:
#     #     main1 = mainexercises[0]
#     #     main2 = mainexercises[1]
#     #     main3 = mainexercises[2]
#     #     main1name=mainexercises[0]
#     #     main2name=mainexercises[1]
#     #     main3name=mainexercises[2]
#     # else:
#     #     main1 = mainexercises[0]
#     #     main2 = mainexercises[1]
#     #     main3 = mainexercises[2]
#     #     main4 =  mainexercises[3] ,('We advise u to reduce the ammount of main exercises!').upper()
#     #     main1name=mainexercises[0]
#     #     main2name=mainexercises[1]
#     #     main3name=mainexercises[2]
#     #     main4name=''
#     #     messages.error(request,('do not fuck around doing more than 3 main exercises!').upper())

    
#     main1 = mainexercises[0].maximalrepetition
#     main2 = mainexercises[1].maximalrepetition
#     main3 = mainexercises[2].maximalrepetition
#     main1name = mainexercises1[0].mainexercise
#     main2name = mainexercises1[1].mainexercise
#     main3name = mainexercises1[2].mainexercise
#     main4name=''
#    #CASUALTRAINING
#     gppsets1=[2,3]
#     gppsets2=[3,4]
#     gpprepsrange1=[16,24]
#     gpprepsrange2=[16,30]
#     #GENERAL PHYSICAL PREPRATION SETS AND REP RANGES and Cas
#     gppsets1=[2,3]
#     gppsets2=[3,4]
#     gpprepsrange1=[16,24]
#     gpprepsrange2=[16,30]
#     gppmain1Iw=[round(main1*0.70),round(main1*0.72,5),round(main1*0.75) ]
#     gppmain1IIw=[round(main1*0.72,5),round(main1*0.75),round(main1*0.77,5)]
#     gppmain2Iw=[round(main2*0.70),round(main2*0.72,5),round(main2*0.75)]
#     gppmain2IIw=[round(main2*0.72,5),round(main2*0.75),round(main2*0.77,5)]
#     gppmain3Iw=[round(main3*0.70),round(main3*0.72,5),round(main3*0.75)]
#     gppmain3IIw=[round(main3*0.72,5),round(main3*0.75),round(main3*0.77,5)]
#     #ACCUMULATION PHASE SETS AND REP RANGES +(INTENSITY= PIREPLIN'S TABLE)
#     # accrepsrange1=[18,30]
#     # accrepsrange2=[12,24]
#     # accrepsrange3=[10,20]
#     # accrepsrange4=[10,18]
#     # accsets1=[3,6]
#     # accsets2=[3,6]
#     # accsets3=[2,4]
#     # accsets4=[2,3]
#     # accsq1w= [round(sq*0.55),round(sq*0.57,5), round(sq*0.60), round(sq*0.62,5), round(sq*0.65)]
#     # accsq2w= [round(sq*0.67,5),round(sq*0.70),round(sq*0.72,5),round(sq*0.75),round(sq*0.77,5)]
#     # accsq3w= [round(sq*0.8),round(sq*0.82,5),round(sq*0.85),round(sq*0.87,5),round(sq*0.9)]
#     # accsq4w= [round(sq*0.5),round(sq*0.52,5),round(sq*0.55),round(sq*0.6)]
#     # accdl1w= [round(dl*0.55),round(dl*0.57,5), round(dl*0.60), round(dl*0.62,5), round(dl*0.65)]
#     # accdl2w= [round(dl*0.67,5),round(dl*0.70),round(dl*0.72,5),round(dl*0.75),round(dl*0.77,5)]
#     # accdl3w= [round(dl*0.8),round(dl*0.82,5),round(dl*0.85),round(dl*0.87,5),round(dl*0.9)]
#     # accdl4w= [round(dl*0.5),round(dl*0.52,5),round(dl*0.55),round(dl*0.6)]
#     # accbp1w= [round(bp*0.55),round(bp*0.57,5), round(bp*0.60), round(bp*0.62,5), round(bp*0.65)]
#     # accbp2w= [round(bp*0.67,5),round(bp*0.70),round(bp*0.72,5),round(bp*0.75),round(bp*0.77,5)]
#     # accbp3w= [round(bp*0.8),round(bp*0.82,5),round(bp*0.85),round(bp*0.87,5),round(bp*0.9)]
#     # accbp4w= [round(bp*0.5),round(bp*0.52,5),round(bp*0.55),round(bp*0.6)]
#     # #PEAK
#     # peakrepsrange1=[8,10]
#     # peakrepsrange2=[5,8]
   
#     # peaksets1=[5,8]
#     # peaksets2=[3,5]
#     # peaksets3=('PEAK', 'MAX OUT!')
#     # peaksets4=('Rest...', 'Start from gpp again')
    
#     # peaksq1w= [round(sq*0.87,5),round(sq*0.9),round(sq*0.92,5), round(sq*0.95) ]
#     # peaksq2w= [round(sq*0.90),round(sq*0.92,5),round(sq*0.95)]
#     # peakdl1w= [round(sq*0.87,5),round(sq*0.9),round(sq*0.92,5), round(sq*0.95)]
#     # peakdl2w= [round(sq*0.90),round(sq*0.92,5),round(sq*0.95)]
#     # peakbp1w= [round(sq*0.87,5),round(sq*0.9),round(sq*0.92,5), round(sq*0.95)]
#     # peakbp2w= [round(sq*0.90),round(sq*0.92,5),round(sq*0.95)]


      
#     if training.mesocycle == "Casual training" or "GPP":
#         a= (f'{gppsets1[0]} - {gppsets1[1]}'),(f'{gpprepsrange1[0]} - {gpprepsrange1[1]}'),(f'{gppmain1Iw[0]}kg, {gppmain1Iw[1]}kg, {gppmain1Iw[2]}kg')
#         b= (f'{gppsets2[0]} - {gppsets2[1]}'),(f'{gpprepsrange2[0]} - {gpprepsrange2[1]}'),(f'{gppmain1IIw[0]}kg, {gppmain1IIw[1]}kg, {gppmain1IIw[2]}kg')
#         c= f''
#         if main2=='':
#             pass
#         else:
#             a1=(f'{gppsets1[0]} - {gppsets1[1]}'),(f'{gpprepsrange1[0]} - {gpprepsrange1[1]}'),(f'{gppmain2Iw[0]}kg, {gppmain2Iw[1]}kg, {gppmain2Iw[2]}kg')
#             b1=(f'{gppsets2[0]} - {gppsets2[1]}'),(f'{gpprepsrange2[0]} - {gpprepsrange2[1]}'),(f'{gppmain2IIw[0]}kg, {gppmain2IIw[1]}kg, {gppmain2IIw[2]}kg')
#         if main2=='':
#             pass
#         else:
#             a2=(f'{gppsets1[0]} - {gppsets1[1]}'),(f'{gpprepsrange1[0]} - {gpprepsrange1[1]}'),(f'{gppmain3Iw[0]}kg, {gppmain3Iw[1]}kg, {gppmain3Iw[2]}kg')
#             b2=(f'{gppsets2[0]} - {gppsets2[1]}'),(f'{gpprepsrange2[0]} - {gpprepsrange2[1]}'),(f'{gppmain3IIw[0]}kg, {gppmain3IIw[1]}kg, {gppmain3IIw[2]}kg')
       
      
        

#         c1=f''
#         c2=f''
#         d= f''
#         d1=f''
#         d2=f''

    
#     # if training.mesocycle == "Acumulation phase":
#     #     a= (f'{accsets1[0]} - {accsets1[1]}'),(f'{accrepsrange1[0]} - {accrepsrange1[1]}'),(f'{accsq1w[0]}kg, {accsq1w[1]}kg, {accsq1w[2]}kg, {accsq1w[3]}kg, {accsq1w[4]}kg')
#     #     a1=(f'{accsets1[0]} - {accsets1[1]}'),(f'{accrepsrange1[0]} - {accrepsrange1[1]}'),(f'{accdl1w[0]}kg, {accdl1w[1]}kg, {accdl1w[2]}kg, {accdl1w[3]}kg, {accdl1w[4]}kg')
#     #     a2=(f'{accsets1[0]} - {accsets1[1]}'),(f'{accrepsrange1[0]} - {accrepsrange1[1]}'),(f'{accbp1w[0]}kg, {accbp1w[1]}kg, {accbp1w[2]}kg, {accbp1w[3]}kg, {accbp1w[4]}kg ')
#     #     b= (f'{accsets2[0]} - {accsets2[1]}'),(f'{accrepsrange2[0]} - {accrepsrange2[1]}'),(f'{accsq2w[0]}kg, {accsq2w[1]}kg, {accsq2w[2]}kg, {accsq2w[3]}kg, {accsq2w[4]}kg')
#     #     b1=(f'{accsets2[0]} - {accsets2[1]}'),(f'{accrepsrange2[0]} - {accrepsrange2[1]}'),(f'{accdl2w[0]}kg, {accdl2w[1]}kg, {accdl2w[2]}kg, {accdl2w[3]}kg, {accdl2w[4]}kg')
#     #     b2=(f'{accsets2[0]} - {accsets2[1]}'),(f'{accrepsrange2[0]} - {accrepsrange2[1]}'),(f'{accbp2w[0]}kg, {accbp2w[1]}kg, {accbp2w[2]}kg, {accbp2w[3]}kg, {accbp2w[4]}kg')
#     #     c= (f'{accsets3[0]} - {accsets3[1]}'),(f'{accrepsrange3[0]} - {accrepsrange3[1]}'),(f'{accsq3w[0]}kg, {accsq3w[1]}kg, {accsq3w[2]}kg, {accsq3w[3]}kg, {accsq3w[4]}kg')
#     #     c1=(f'{accsets3[0]} - {accsets3[1]}'),(f'{accrepsrange3[0]} - {accrepsrange3[1]}'),(f'{accdl3w[0]}kg, {accdl3w[1]}kg, {accdl3w[2]}kg, {accdl3w[3]}kg, {accdl3w[4]}kg')
#     #     c2=(f'{accsets3[0]} - {accsets3[1]}'),(f'{accrepsrange3[0]} - {accrepsrange3[1]}'),(f'{accbp3w[0]}kg, {accbp3w[1]}kg, {accbp3w[2]}kg, {accbp3w[3]}kg, {accbp3w[4]}kg')
#     #     d= (f'{accsets4[0]} - {accsets4[1]}'),(f'{accrepsrange4[0]} - {accrepsrange4[1]}'),(f'{accsq4w[0]}kg, {accsq4w[1]}kg, {accsq4w[2]}kg, {accsq4w[3]}kg')
#     #     d1=(f'{accsets4[0]} - {accsets4[1]}'),(f'{accrepsrange4[0]} - {accrepsrange4[1]}'),(f'{accdl4w[0]}kg, {accdl4w[1]}kg, {accdl4w[2]}kg, {accdl4w[3]}kg')
#     #     d2=(f'{accsets4[0]} - {accsets4[1]}'),(f'{accrepsrange4[0]} - {accrepsrange4[1]}'),(f'{accbp4w[0]}kg, {accbp4w[1]}kg, {accbp4w[2]}kg, {accbp4w[3]}kg')


#     # if training.mesocycle == "Peak phase":
#     #     a= (f'{peaksets1[0]} - {peaksets1[1]}'),(f'{peakrepsrange1[0]} - {peakrepsrange1[1]}'),(f'{peaksq1w[0]}kg, {peaksq1w[1]}kg, {peaksq1w[2]}kg,  {peaksq1w[3]}kg')
#     #     a1=(f'{peaksets1[0]} - {peaksets1[1]}'),(f'{peakrepsrange1[0]} - {peakrepsrange1[1]}'),(f'{peakdl1w[0]}kg, {peakdl1w[1]}kg, {peakdl1w[2]}kg,  {peakdl1w[2]}kg')
#     #     a2=(f'{peaksets1[0]} - {peaksets1[1]}'),(f'{peakrepsrange1[0]} - {peakrepsrange1[1]}'),(f'{peakbp1w[0]}kg, {peakbp1w[1]}kg, {peakbp1w[2]}kg,  {peakbp1w[2]}kg')
#     #     b= (f'{peaksets2[0]} - {peaksets2[1]}'),(f'{peakrepsrange2[0]} - {peakrepsrange2[1]}'),(f'{peaksq2w[0]}kg, {peaksq2w[1]}kg, {peaksq2w[2]}kg')
#     #     b1=(f'{peaksets2[0]} - {peaksets2[1]}'),(f'{peakrepsrange2[0]} - {peakrepsrange2[1]}'),(f'{peakdl2w[0]}kg, {peakdl2w[1]}kg, {peakdl2w[2]}kg')
#     #     b2=(f'{peaksets2[0]} - {peaksets2[1]}'),(f'{peakrepsrange2[0]} - {peakrepsrange2[1]}'),(f'{peakbp2w[0]}kg, {peakbp2w[1]}kg, {peakbp2w[2]}kg')
#     #     c=(str(peaksets3[0]),"",str(peaksets3[0]))
#     #     c1=(str(peaksets3[0]),"",str(peaksets3[1]))
#     #     c2=(str(peaksets3[0]),"",str(peaksets3[0]))
#     #     d= ()
#     #     d1=()
#     #     d2=str(peaksets4[0]),"",str(peaksets4[1])




   

#     context = {'training':training ,'mainexercises': mainexercises,
#     'main1':main1,'main2':main2,'main3':main3,'main4':main4,
#     'main1name':main1name,'main2name':main2name,'main3name':main3name,
#     'main4name':main4name,
#     'trainingun':trainingun,
#     'a':a,'a1':a1,'a2':a2 ,'b':b,'b1':b1,'b2':b2, 'c':c,'c1':c1,
#     'c2':c2, 'd':d, 'd1':d1,'d2':d2 ,
#     }    
#     return render(request, 'core/trainingplansecond.html',context)