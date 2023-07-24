from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now = True) #auto_now makes field uneditable (won't appear in database)
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
    )

    def __str__(self): # Every method in on a Python class takes "self" as its first parameter
        return self.text[0:100] #Limit post title to 100 characters