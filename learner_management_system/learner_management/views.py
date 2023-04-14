from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from .models import personal_Information, address, certificates, education, experience, placement, Users


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
    if request.method == 'POST':
        # save personal info data to database
         personalinfo = personal_Information()
         personalinfo.first_name = request.POST.get('first_name')
         personalinfo.last_name = request.POST.get('last_name')
         personalinfo.date_of_birth = request.POST.get('date_of_birth')
         personalinfo.id_passport_no = request.POST.get('id_passport_no')
         personalinfo.email_address = request.POST.get('email_address')
         personalinfo.contact_num = request.POST.get('contact_num')
         personalinfo.profession = request.POST.get('profession')
         personalinfo.profile_pic = request.FILES.get('profile_pic')
         personalinfo.personal_summary = request.POST.get('personal_summary')
         personalinfo.save()
         return redirect('academicinfo')
    else:
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