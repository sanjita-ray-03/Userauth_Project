from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import signup_view, login_view, patient_dashboard, doctor_dashboard

app_name = 'accounts'

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('patient-dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor-dashboard/', doctor_dashboard, name='doctor_dashboard'),
    #  path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]



