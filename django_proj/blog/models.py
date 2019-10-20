from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # pass function to be called when quired
    author = models.ForeignKey(User, on_delete=models.CASCADE) # CASCADE user delete to posts

    def __str__(self):
        return self.title