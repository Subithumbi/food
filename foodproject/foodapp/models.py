from django.db import models

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=250)
    ing=models.TextField()
    recipie=models.TextField()
def __str__(self):
    return self.name