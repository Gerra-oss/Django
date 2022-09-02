from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 20)
    address = models.CharField(max_length = 20)
    created = models.DateField(auto_now_add = True)

    class Meta:
        ordering = ['created']
