
from django.contrib import messages
from django.shortcuts import render,redirect
from core.forms import ExerciseForm, TrainingForm , TrainingUnitForm, NewbieExercise,NewbieTrainingForm,MainExerciseForm, NewbieExerciseForm,NewbieTrainingUnitForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from core.models import MainExercise, TrainingPlan,Exercise, TrainingUnit , NewbieExercise,NewbieTrainingPlan,NewbieTrainingUnit
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def registerPage(request):
    form = UserCreationForm()

    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username= user.username.lower()
            user.save()
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'error (check if password matches ,or characters are valid)')

    return render (request , 'login_register.html',{'form':form})

def logpage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect ('homepage')
    
    if request.method =='POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username is not valid')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request,'password is not valid')

    context ={'page':page}
    return render(request,'core/login_register.html',context)


def logoutUser(request):
    logout(request)
    return redirect('homepage')



def HomePage(request):
    treningi = TrainingPlan.objects.all()
    treninginoperio= NewbieTrainingPlan.objects.all()
    context = {'treningi': treningi,'treninginoperio': treninginoperio}
    return render(request, 'core/homepage.html',context)


def ProfilePage(request,pk):
    profile=''
    context= {'profile':profile}
    return render(request, 'core/profilepage.html',context)

trainingplans=[]
exercises=[]

def TrainingPlanForUser(request,pk):
    trainingunit=''
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
    peaksets4=('Rest...', 'Start from GPP again')
    
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
        d2=()


    #training = TrainingPlan.objects.get(id=pk)
  
    
    trainingunits=training.trainingunit_set.all()  # type: ignore
    exercises = TrainingUnit.objects.values('exercise').filter(trainingplan=pk)

    exerintu= TrainingUnit.objects.all().filter(trainingplan=pk)
  
    day1firstexercise= exercises



    
        
    context={ 'a':a,'a1':a1,'a2':a2 ,'b':b,'b1': b1,'b2':b2, 'c':c,'c1':c1,
    'c2':c2, 'd':d, 'd1':d1,'d2':d2 ,'sq':sq,'dl':dl,'bp':bp, 'exercises':exercises ,
    'training': training,
    'mesocycle': mesocycle,
    'training.mesocycle': training.mesocycle,'exercise':exercise,'trainingunits':trainingunits,'exerintu':exerintu, 'trainingunit':trainingunit,
       'day1firstexercise': day1firstexercise}

    return render(request, 'core/trainingplan.html',context)

def TrainingUnitInPlan(request,pk):
    exercise=''
    trainingunit=TrainingUnit.objects.get(id=pk)
    exercises = trainingunit.exercise_set.all()  # type: ignore

    if request.method =="POST":
        exercise = ExerciseForm(request.POST)
        if exercise.is_valid():
            exercise=Exercise.objects.create(
            trainingunit=TrainingUnit.objects.get(id=pk),
            exercisename=request.POST.get('exercisename'),
            exercisesets=request.POST.get('exercisesets'),
            exercisereps=request.POST.get('exercisereps'),
            )
       

    context= {'trainingunit':trainingunit,'exercises':exercises ,'exercise':exercise }
    return render(request, 'core/trainingunit.html',context)

def AddTrainingPlan(request):
    training = TrainingForm()

    if request.method =="POST":
        training = TrainingForm(request.POST)
        if training.is_valid():
            trainingplans.append(training)
            training.user=request.user  # type: ignore
            training.save()
            return redirect('homepage')
        context= {'training': training}

        return render(request,'core/addtrainingplan.html', context)
    else:
        return render(request, 'core/addtrainingplan.html', {"training": training})   





def TrainingPlanFreelance(request,pk):
    trainingunit=''
    trainingplan = NewbieTrainingPlan.objects.get(id=pk)
    trainingunits= trainingplan.newbietrainingunit_set.all()  # type: ignore


    if request.method =="POST":
        trainingunit = NewbieTrainingUnitForm(request.POST)
        if trainingunit.is_valid():
            trainingunit=NewbieTrainingUnit.objects.create(
            trainingplan=NewbieTrainingPlan.objects.get(id=pk),
            name=request.POST.get('name'),
          )


    context = {'trainingplan':trainingplan,'trainingunit':trainingunit,'trainingunits': trainingunits}
    

    return render(request, 'core/trainingplanfreelance.html',context)

def AddTrainingPlanFreelance(request):
    training = NewbieTrainingForm()

    if request.method =="POST":
        training = NewbieTrainingForm(request.POST)
        if training.is_valid():
            trainingplans.append(training)  # type: ignore
            training.user=request.user  # type: ignore
            training.save()
            return redirect('homepage')
        context= {'training': training}

        return render(request,'core/addtrainingfreelance.html', context)
    else:
        return render(request, 'core/addtrainingfreelance.html', {"training": training})   

def TrainingUnitInPlanFreelance(request,pk):
    mainexercise=''
    exercise=''
    trainingunit = NewbieTrainingUnit.objects.get(id=pk)
    exercises = trainingunit.newbieexercise_set.all()  # type: ignore
    mainexercises = trainingunit.mainexercise_set.all()  # type: ignore

    if request.method =="POST":
        exercise = NewbieExerciseForm(request.POST)
        if exercise.is_valid():
            exercise=NewbieExercise.objects.create(
            trainingunit=NewbieTrainingUnit.objects.get(id=pk),
            exercisename=request.POST.get('exercisename'),
            exercisesets=request.POST.get('exercisesets'),
            exercisereps=request.POST.get('exercisereps'),
            )

    if request.method =="POST":
        mainexercise = MainExerciseForm(request.POST)
        if mainexercise.is_valid():
            mainexercise=MainExercise.objects.create(
            trainingunit=NewbieTrainingUnit.objects.get(id=pk),
            mainexercise=request.POST.get('mainexercise'),
            exercisesets=request.POST.get('exercisesets'),
            exercisereps=request.POST.get('exercisereps'),
            intensity= request.POST.get('intensity'),
            )


    context= {'trainingunit':trainingunit,'mainexercise': mainexercise, 'mainexercises': mainexercises, 'exercise':exercise ,'exercises':exercises,}
    return render(request, 'core/trainingunitfreelance.html',context)



def render_pdf_view(request,pk):

    template_path = 'core/renderpdf.html'
    trainingunit=''
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
    peaksets4=('Rest...', 'Start from GPP again')
    
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
        d2=()


    #training = TrainingPlan.objects.get(id=pk)

    trainingunits=training.trainingunit_set.all()  # type: ignore
    exercises = TrainingUnit.objects.values('exercise').filter(trainingplan=pk)

    exerintu= TrainingUnit.objects.all().filter(trainingplan=pk)

    day1firstexercise= exercises
    
    context={ 'a':a,'a1':a1,'a2':a2 ,'b':b,'b1': b1,'b2':b2, 'c':c,'c1':c1,
    'c2':c2, 'd':d, 'd1':d1,'d2':d2 ,'sq':sq,'dl':dl,'bp':bp, 'exercises':exercises ,
    'training': training,
    'mesocycle': mesocycle,
    'training.mesocycle': training.mesocycle,'exercise':exercise,'trainingunits':trainingunits,'exerintu':exerintu, 'trainingunit':trainingunit,
    'day1firstexercise': day1firstexercise}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #for download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] =  'filename="renderpdf.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




def render_pdf_view_nonperiodized(request,pk):
    template_path = 'core/renderpdfnotperiodized.html'
    trainingunit=''
    trainingplan = NewbieTrainingPlan.objects.get(id=pk)
    trainingunits= trainingplan.newbietrainingunit_set.all()  # type: ignore


    context = {'trainingplan':trainingplan,'trainingunit':trainingunit,'trainingunits': trainingunits}
    response = HttpResponse(content_type='application/pdf')
    #for download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] =  'filename="renderpdf.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


