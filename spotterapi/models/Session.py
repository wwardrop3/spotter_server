from django.db import models

from spotterapi.models.Exercise import Exercise

class Session(models.Model):
    plan = models.ForeignKey("Plan", on_delete = models.CASCADE)
    exercises = models.ManyToManyField(Exercise, through = "SessionExercise")
    