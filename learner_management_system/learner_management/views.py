from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def home(request):
    return HttpResponse('<h1>welcome</h1>')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()

        
    return render(request,'learner_management/register.html',{'form':form})

def personalinfo(request):
    return render(request,'learner_management/personalinfo.html')

def academic_info(request):
    return render(request,'learner_management/education.html')

def workhistory_info(request):
    return render(request,'learner_management/workhistory.html')

def learnerhome(request):
    return render(request, 'learner_management/home.html')

def personal_summary(request):
    # your login view logic here...
    return render(request, 'learner_management/summary.html')

def login_view(request):
    # your login view logic here...
    return render(request, 'learner_management/login.html')

def register_view(request):
    # your login view logic here...
    return render(request, 'learner_management/register.html')

def learner_cv(request):
    return render(request,'learner_management/learnercv.html')