from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField(max_length=11)

    def __str__(self):
        return self.name
    
class Animal(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1)
    dob = models.DateField(max_length=10)
    weight = models.FloatField(max_length=5, blank=True, null=True)
    is_alive = models.BooleanField()
    owner_id = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
