from django.db import models

# Create your models here.

class victim(models.Model):
    name = models.CharField(max_length=100)
    ic = models.CharField(max_length=100)
    number = models.CharField(max_length=15)

    def __str__(self):
        return (self.name + ' ' + self.ic)
    