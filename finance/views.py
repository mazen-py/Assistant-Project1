from django.shortcuts import render
from .models import Account, Transaction, PlannedPayment
from django.db.models import Sum

def finance_home(request):
    # 1. Get all accounts and calculate the grand total
    accounts = Account.objects.all()
    total_balance = sum(account.balance for account in accounts)

    # 2. Get the 10 most recent transactions
    transactions = Transaction.objects.all().order_by('-date')[:10]

    # 3. Calculate total income and total expenses
    income_total = Transaction.objects.filter(is_income=True).aggregate(Sum('amount'))['amount__sum'] or 0
    expense_total = Transaction.objects.filter(is_income=False).aggregate(Sum('amount'))['amount__sum'] or 0

    # 4. Get upcoming planned payments
    planned_payments = PlannedPayment.objects.all().order_by('due_date')[:5]

    context = {
        'accounts': accounts,
        'total_balance': total_balance,
        'transactions': transactions,
        'income_total': income_total,
        'expense_total': expense_total,
        'planned_payments': planned_payments,
    }
    return render(request, 'finance/home.html', context)