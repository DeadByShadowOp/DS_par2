from django.db import models
import moneyed
from djmoney.models.fields import MoneyField
from payments.money import Money
from polymorphic.models import PolymorphicModel
from functools import reduce
# Create your models here.
# ok


class Restaurant(models.Model):
    name = models.CharField(max_length=50, unique=True)


class BasePlate(PolymorphicModel):
    id = models.AutoField(primary_key=True)
    sopa = models.CharField(max_length=150)
    segundo = models.CharField(max_length=150)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)


class StudentsPlate(BasePlate):
    price = MoneyField(max_digits=10, decimal_places=2,
                       default_currency='USD', default=Money(2.5, 'USD'))

    def get_total_price(self):
        return self.price


class ExecutivePlate(BasePlate):
    price = MoneyField(max_digits=10, decimal_places=2,
                       default_currency='USD', default=Money(3, 'USD'))

    def get_total_price(self):
        total = self.price 
        for extra in Extra.objects.filter(plate=self).all():
          total += extra.price
        return total

    def get_extras(self):
        extras = Extra.objects.filter(plate=self).all()
        extrastr = ""
        for extra in extras:
          extrastr += extra.name + ","
        return extrastr

class Extra(models.Model):
    price = MoneyField(max_digits=10, decimal_places=2,
                       default_currency='USD')
    name = models.CharField(max_length=40)
    plate = models.ForeignKey('ExecutivePlate', on_delete=models.CASCADE)
