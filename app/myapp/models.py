from django.db import models


# Create your models here.
class Person(models.Model):
    SHIRT_SIZE = (
        ('S', 'SMALL'),
        ('M', 'MEDIUM'),
        ('L', 'LARGE'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' '+ self.last_name
