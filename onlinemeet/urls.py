from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-meetings/', views.meeting_list, name='meeting_list'),
    path('live-meeting/<unique_meeting_name>/', views.meeting, name='meeting'),

]