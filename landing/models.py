from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=32)

    def __str__(self):
        return f'Email: {self.email} and name: {self.name}'