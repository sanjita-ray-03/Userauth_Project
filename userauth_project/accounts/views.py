from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import CustomUser

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=user.username, password=raw_password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, 'Signup successful!')

                if user.user_type == 'patient':
                    return render(request ,'accounts/patient_dashboard.html', {'first_name': user.first_name, 'last_name': user.last_name, 'email' : user.email, 'address_line1': user.address_line1, 'city' : user.city, 'state': user.state , 'pincode': user.pincode})
                elif user.user_type == 'doctor':
                    return render(request, 'accounts/doctor_dashboard.html', {'first_name': user.first_name, 'last_name': user.last_name, 'email' : user.email, 'address_line1': user.address_line1, 'city' : user.city, 'state': user.state , 'pincode': user.pincode})
            else:
                messages.error(request, "Login after signup failed.")
        else:
            messages.error(request, 'Signup failed. Please fix the errors.')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/signup.html', {'user_form': form,
    'profile_form': form,})



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'patient':
                return render(request ,'accounts/patient_dashboard.html', {'first_name': user.first_name, 'last_name': user.last_name, 'email' : user.email, 'address_line1': user.address_line1, 'city' : user.city, 'state': user.state , 'pincode': user.pincode})
            elif user.user_type == 'doctor':
                return render(request, 'accounts/doctor_dashboard.html', {'first_name': user.first_name, 'last_name': user.last_name, 'email' : user.email, 'address_line1': user.address_line1, 'city' : user.city, 'state': user.state , 'pincode': user.pincode})
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')
