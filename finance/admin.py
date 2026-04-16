from django.contrib import admin
from .models import Account, Transaction, PlannedPayment

admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(PlannedPayment)