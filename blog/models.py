from django.db import models
from django.utils import timezone

# Create your models here.

class Project(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    initdate = models.DateTimeField()
    finaldate = models.DateTimeField()
    
    def __str__(self):
        return self.title
