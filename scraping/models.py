from django.db.models import *
from django.utils import timezone


class Job(Model):
    name = CharField(max_length=250)
    numbers = CharField(max_length=250)
    ExchangeRates = DecimalField(max_digits=10, decimal_places=2, null=False)
    created_date = DateTimeField(default=timezone.now)

    # @property
    # def formatted_price(self):
    #     return f'{self.ExchangeRates}'
