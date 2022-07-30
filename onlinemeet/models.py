from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify
import datetime


class Meeting(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # creator of the meeting
    title_of_meeting = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)  # the time meeting was created
    updated = models.DateTimeField(auto_now=True)  # time meeting was updated
    starting_date_time = models.DateTimeField()
    unique_meeting_name = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s: %s' % (self.creator, self.title_of_meeting)

    def save(self, *args, **kwargs):
        if not self.unique_meeting_name:
            self.unique_meeting_name = slugify(
                str(self.title_of_meeting) + '-' + str(uuid.uuid4())
            )
        return super(Meeting, self).save()

    @property
    def meeting_time(self):
        '''
        this is a model property for checking if it is meeting time. we shall be using
        this in the template
        '''
        return (datetime.datetime.now() >= self.starting_date_time) and (
                datetime.datetime.now() <= self.ending_date_time
        )