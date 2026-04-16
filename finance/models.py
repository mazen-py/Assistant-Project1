from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=50) # e.g., "Cash", "Bank account"
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    is_income = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.description} - {self.amount}"

class PlannedPayment(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_repeatable = models.BooleanField(default=False)

    def __str__(self):
        return self.description