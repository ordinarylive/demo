from django.db import models

# Create your models here.

class Follow(models.Model):
    uid=models.CharField()
    fid=models.CharField()

