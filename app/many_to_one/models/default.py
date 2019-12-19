from django.db import models


# Create your models here.
class Manufacture(models.Model):
    name = models.CharField('제조사명', max_length=20)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacture = models.ForeignKey(
        Manufacture,  # Foreign Key 로 가리킬 다른 모델명
        on_delete=models.CASCADE
    )
    name = models.CharField('차량명', max_length=100)

    def __str__(self):
        return self.name
