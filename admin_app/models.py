from django.db import models

# Create your models here.

class designation(models.Model):
    designation = models.CharField(max_length=100)
    files=models.FileField(upload_to = 'images/', null=True, blank=True)
    status = models.CharField(max_length=100)
    total_count = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.designation