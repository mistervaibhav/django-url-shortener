from django.db import models

# Create your models here.
class Url(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=100)

    
