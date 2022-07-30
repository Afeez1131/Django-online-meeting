from django.shortcuts import render, HttpResponseRedirect
from .forms import MeetingCreateForm
from .models import Meeting
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages


def home(request):
    form = MeetingCreateForm()
    if request.method == 'POST':
        form = MeetingCreateForm(request.POST)
        if form.is_valid():
            fm = form.save(commit=False)
            # since in our form, we do not want to be selecting users,
            # we have to set the creator as the current user.
            fm.creator = request.user
            fm.save()
            return HttpResponseRedirect(reverse('meeting_list'))

    return render(request, 'onlinemeet/home.html', {'form': form})


@login_required()  # to ensure only logged in user can view this page.
def meeting_list(request):
    """We are going to filter the meeting, so only the registered user can view
    the page, and then all meeting created by such individual will be displayed"""
    user = request.user
    meetings = Meeting.objects.filter(creator=user)

    return render(request, 'onlinemeet/meeting_list.html', {'meetings': meetings})


def meeting(request, unique_meeting_name):
    meeting = Meeting.objects.get(unique_meeting_name=unique_meeting_name)

    return render(request, 'onlinemeet/meeting_page.html', {'meeting': meeting})
