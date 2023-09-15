from django.db import models

# Create your models here.
class products(models.Model):
 name=models.CharField(max_length=200)
 image=models.ImageField()
 def __str__(self) -> str:
  return self.name

