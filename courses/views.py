from django.shortcuts import render
from .models import Course,Lesson
from django.contrib.auth.decorators import login_required

@login_required(login_url="landing:login")
def courseHome(request):
    courses=Course.objects.all()
    context={'courses':courses}
    return render(request,'courses/all_courses.html',context)
