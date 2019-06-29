from django.db import models
from django.utils import timezone

# Create your models here.

class Formation(models.Model):
    course = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    initdate = models.DateTimeField()
    finaldate = models.DateTimeField()
    def __str__(self):
        return self.course

class Experience(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    ocupation = models.CharField(max_length=100)
    description = models.TextField()
    initdate = models.DateTimeField(null=True, blank=True)
    finaldate = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.title

