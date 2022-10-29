from django.db import models

from spotterapi.models.Exercise import Exercise

class Plan(models.Model):
    name = models.TextField()
    exercises = models.ManyToManyField(Exercise, through = "PlanExercise")
