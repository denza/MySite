from django.db import models
from django.urls import reverse
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User

class Question(models.Model):
    quest_name = models.CharField(max_length = 100)
    quest_text = models.CharField(max_length = 50000)
    pub_date = models.DateTimeField(auto_now_add=True)
    
   

    def __str__(self):
        return self.quest_name
    
    def get_absolute_url(self):
        return reverse("postovi:detail", kwargs={"pk": self.pk}) 
    

class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    comment_text = models.CharField(max_length = 50000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_text
    
