from django.contrib.auth.models import User
from django.db import models


# TODO move
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# TODO move
# TODO function to add default (USD, CHF, EUR) - https://docs.djangoproject.com/en/1.10/howto/initial-data/
class Currency(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)


class Transaction(models.Model):
    description = models.TextField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.ForeignKey(Currency, related_name='currency')
    debtor = models.ForeignKey(User, related_name='debtor')
    creditor = models.ForeignKey(User, related_name='creditor')
    date_created = models.DateTimeField('date_created')
    deleted = models.BooleanField()
    date_deleted = models.DateTimeField('date_deleted')
