from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    # due = models.DateTimeField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # shared users

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('todo_list')
