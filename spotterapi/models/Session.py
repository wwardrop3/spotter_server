from django.db import models

from spotterapi.models.Exercise import Exercise

class Session(models.Model):
    profile = models.ForeignKey("Profile", on_delete = models.CASCADE)
    exercises = models.ManyToManyField(Exercise, through = "SessionExercise")
    plan = models.ForeignKey("Plan", on_delete=models.CASCADE)
    from_plan = models.BooleanField(True)
    start_date = models.DateTimeField()
    
    
