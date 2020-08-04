from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserSignupForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

def home(request):
    return render(request,'landing/body.html')

def terms(request):
    return render(request,'landing/terms.html')

def about(request):
    return render(request,'landing/about.html')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('landing:home') 
    else:
        if request.method =="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('courses:all_courses')
            else:
                messages.info(request,"Username os Password is incorrect")

        return render(request,'landing/login.html')


def logoutUser(request):
    logout(request)
    return redirect('landing:home')


def signupUser(request):
    if request.user.is_authenticated:
        return redirect('landing:home')
    else:

        form=UserSignupForm()

        if request.method == 'POST':
            form=UserSignupForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get("username")
                messages.success(request,user+", Your Account has been successfully created! Login To continue ")
                return redirect('landing:login')

        context={'form':form}
        return render(request,'landing/signup.html',context)
