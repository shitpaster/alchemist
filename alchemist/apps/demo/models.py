from django.db import models

# Create your models here.
class DemoMessage(models.Model):
    text = models.TextField()