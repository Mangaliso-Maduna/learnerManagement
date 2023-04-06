from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'learner_management'

urlpatterns = [
    path('',views.home, name='home'),
    
    path('summary/learnercv/', RedirectView.as_view(url='/learnercv/', permanent=True)),
    path('learnercv/', views.learner_cv, name='learnercv'),
    path('login/',auth_views.LoginView.as_view(template_name='learner_management/login.html'),name='login'),
    path('register/',views.register,name='register'),
    path('logout/',auth_views.LogoutView.as_view(template_name='learner_management/login.html'),name='logout'),
    
    path('learnerhome/personalinfo/', RedirectView.as_view(url='/personalinfo/', permanent=True)),
    path('personalinfo/',views.personalinfo,name='personalinfo'),
    
    
    path('academicinfo/personalinfo/', RedirectView.as_view(url='/personalinfo/', permanent=True)),
    path('learnerhome/academicinfo/', RedirectView.as_view(url='/academicinfo/', permanent=True)),
    path('personalinfo/academicinfo/', RedirectView.as_view(url='/academicinfo/', permanent=True)),
    path('academicinfo/',views.academic_info,name='academic_info'),

    path('academicinfo/workexperience/', RedirectView.as_view(url='/workexperience/', permanent=True)),
    path('summary/workexperience/', RedirectView.as_view(url='/workexperience/', permanent=True)),
    path('workexperience/',views.workhistory_info,name='workhistory_info'),
    
    
    
    
    path('workexperience/summary/', RedirectView.as_view(url='/summary/', permanent=True)),
    path('summary/',views.personal_summary,name='personal_summary'),

    path('register/login/', RedirectView.as_view(url='/login/', permanent=True)),
    path('login/', views.login_view, name='login'),
    path('login/register/', RedirectView.as_view(url='/register/', permanent=True)),
    path('register/', views.register_view, name='register'),
    path('login/learnerhome/', RedirectView.as_view(url='/learnerhome/', permanent=True)),
    path('learnerhome/',views.learnerhome,name='learnerhome'),
    
]


urlpatterns+= staticfiles_urlpatterns()

