from django.db import models
from django.contrib.auth.models import User  # Import the User model

# Create your models here.

class Birthday(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    
    def __str__(self):
        return self.name
