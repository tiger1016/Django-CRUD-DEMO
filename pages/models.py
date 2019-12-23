from django.db import models

# Create your models here.

class Page(models.Model):
    page = models.CharField(max_length = 20, unique = True)
