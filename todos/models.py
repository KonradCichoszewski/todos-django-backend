from django.db import models

# Create your models here.

class Todo (models.Model):
  class Meta:
    ordering = ['-id']
  
  text = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)

  