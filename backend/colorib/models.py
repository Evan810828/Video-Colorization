from django.db import models

# Create your models here.
class imgCode(models.Model):
  code = models.CharField(max_length=50000)