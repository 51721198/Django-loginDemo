from django.db import models


# Create your models here.

class UserInformation(models.Model):
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


class Hospital(models.Model):
    hostpital_number = models.IntegerField()
    hospital_name = models.CharField(max_length=30)
    hospital_phone = models.CharField(max_length=15)
    hospital_address = models.CharField(max_length=100)


class LicenseDetail(models.Model):
    serial_number_id = models.IntegerField()
    source_number = models.CharField(max_length=30)
    create_date = models.DateTimeField()
    expired_date = models.DateTimeField()
    encrypted_number = models.CharField(max_length=100)
    hospital_number = models.IntegerField()
    license_state = models.IntegerField()
    key_id = models.IntegerField()


class RSAKey(models.Model):
    key_id = models.IntegerField()
    private_key = models.BinaryField()
    public_key = models.BinaryField()
