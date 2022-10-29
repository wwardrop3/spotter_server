from django.db import models

class PlanExercise(models.Model):
    plan = models.ForeignKey("Plan", on_delete=models.CASCADE)
    exercise = models.ForeignKey("Exercise", on_delete = models.CASCADE)
    reps = models.IntegerField()
    weight = models.IntegerField()
    distance = models.IntegerField()