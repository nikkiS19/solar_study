from django.urls import path
from . import views

app_name ='courses'

urlpatterns = [
    path('',views.courseHome,name='all_courses'),
]


