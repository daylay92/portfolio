from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200, null=False)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    body= models.TextField(null=False)
    image= models.ImageField(upload_to='images')