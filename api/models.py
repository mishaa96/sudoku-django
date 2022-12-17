from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CHOICES = [
    ('E', 'Easy'),
    ('M', 'Medium'),
    ('H', 'Hard')
]


class Puzzle(models.Model):
    puzzle = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    mode = models.CharField(choices=CHOICES, default="E", max_length=1)
    timer = models.IntegerField(default=0)
    size = models.IntegerField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.mode