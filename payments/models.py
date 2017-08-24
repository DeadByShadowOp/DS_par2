from django.db import models
import moneyed
from djmoney.models.fields import MoneyField
from .money import Money
from datetime import date
from django.conf import settings
from polymorphic.models import PolymorphicModel

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plate_limit = models.Q(app_label='restaurantes', model='StudentsPlate') | models.Q(
        app_label='restaurantes', model='ExecutivePlate')
    plate_content_type = models.ForeignKey(
        ContentType, related_name='plate_content_type', limit_choices_to=plate_limit)
    plate_object_id = models.PositiveIntegerField()
    plate = GenericForeignKey('plate_content_type', 'plate_object_id')
    pickup_time = models.TimeField()
    order_id = models.AutoField(primary_key=True)
    payment_limit = models.Q(app_label='payments', model='CreditCardPaymentMethod') | models.Q(
        app_label='payments', model='SmartCardPaymentMethod')
    payment_object_id = models.PositiveIntegerField()
    payment_content_type = models.ForeignKey(
        ContentType, related_name='payment_content_type', limit_choices_to=payment_limit)
    payment_type = GenericForeignKey(
        'payment_content_type', 'payment_object_id')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_order_total(self):
        return self.plate.get_total_price()

    def __str__(self):
        return self.order_id


class PaymentMethod(PolymorphicModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = MoneyField(max_digits=10, decimal_places=2,
                         default_currency='USD', default=Money(0.0, 'USD'))

    def pay(self, amount):
        if(amount > self.balance):
            return "Cannot Pay."
        self.balance = self.balance - amount
        return "Paid."

    class Meta:
        abstract = True


class CreditCardPaymentMethod(PaymentMethod):
    card_number = models.CharField(max_length=16)
    ccv = models.CharField(max_length=3)
    expiry_date = models.DateField()

    def pay(self, amount):
        if(self.expiry_date < date.today()):
            return "Cannot Pay."
        return "Will be paid."


class PaymentGateway(models.Model):

    def processPayment(self, payment_method, amount):
        return payment_method.pay(amount)

