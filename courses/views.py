from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="landing:login")
def courseHome(request):
    return render(request,'courses/all_courses.html')
