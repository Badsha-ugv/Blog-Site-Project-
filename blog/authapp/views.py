from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,UpdateProfile,UpdateProfilePic

# Create your views here.


def sign_up(request):
    form = SignUpForm()
    register = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            register = True
    dict = {'form':form,'register':register}
    return render(request,'auth/sign_up.html',dict)

def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    dict = {'form':form}
    return render(request,'auth/log_in.html',dict)

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def profile(request):
    return render(request,'auth/profile.html')

@login_required
def update_profile(request):
    current_user = request.user
    form = UpdateProfile(instance=current_user)
    if request.method == 'POST':
        form = UpdateProfile(request.POST,instance=current_user)
        if form.is_valid():
            form.save()
            form = UpdateProfile(instance=current_user)
    dict = {'form':form}
    return render(request,'auth/update_profile.html',dict)

def update_profile_pic(request):
    form = UpdateProfilePic()
    dict = {'form':form }
    return render(request,'auth/update_profile_pic.html',dict)
