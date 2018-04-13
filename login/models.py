from django.db import models


# Create your models here.

class Userinformation(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    uid = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]

    class Admin:
        list_display = ('name', 'age', 'email')
