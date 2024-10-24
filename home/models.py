from django.db import models
from django.contrib.auth.models import User  

class Blog(models.Model):  
    topic = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='blogs') 

    def __str__(self):
        return self.topic
