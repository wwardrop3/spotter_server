from django.db import models

class Exercise(models.Model):
    name = models.TextField()
    machine = models.ForeignKey("Machine", on_delete = models.CASCADE)
    body_part = models.ForeignKey("BodyPart", on_delete = models.CASCADE)
    type = models.ForeignKey("Type", on_delete = models.CASCADE)
    
    
    