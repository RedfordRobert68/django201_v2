from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=240)
    date = models.DateTimeField(auto_now = True) #auto_now makes field uneditable (won't appear in database)

    def __str__(self): # Every method in on a Python class takes "self" as its first parameter
        return self.text[0:100] #Limit post title to 100 characters