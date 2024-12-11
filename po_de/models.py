from django.db import models

# Create your models here.
class Post(models.Model):
  tille=models.CharField(max_length=200)
  comment=models.TextField()
  author=models.TextField()

  def __str__(self):
    return  {self.title}