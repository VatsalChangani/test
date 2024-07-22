from django.db import models

class Blog(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    repeat_password = models.CharField(max_length=100)
    
   #class Meta:
       # ordering = ['created']