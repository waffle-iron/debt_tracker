from django.contrib.auth.models import User
from django.db import models


class Transaction(models.Model):
    description = models.TextField
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.TextField
    # TODO why?
    debtor = models.ForeignKey(User, related_name='debtor')
    creditor = models.ForeignKey(User, related_name='creditor')
    date_created = models.DateTimeField('date published')
    deleted = models.BooleanField
    date_deleted = models.DateTimeField('date published')


# TODO move
class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
