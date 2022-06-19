from telnetlib import STATUS
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    Author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='Blog_post')
    Created_date = models.DateTimeField(auto_now=True)
    Published_date = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ['created_on'] 


def _str_(self):
    return self.title     
# Create your models here.
