from django.db import models

# Create your models here.

class testblog(models.Model):
    title=models.CharField(max_length=200)
    body=models.CharField(max_length=200)

    def __str__(self):
        return f"title={self.title} body={self.body}"
