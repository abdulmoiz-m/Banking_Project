from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import TransactionForm
from .models import Transaction


# Create your views here.
def homepage(request):
    return render(request, 'bestbank/homepage.html')


@login_required(login_url='login')
# balance and transactions
def overview(request):
    query = Transaction()
    transactions = Transaction.objects.filter(from_user=request.user) | Transaction.objects.filter(to_user=request.user)
    context = {'transactions': transactions, 'user': request.user}
    return render(request, 'bestbank/overview.html', context)


@login_required(login_url='login')
def transfer(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.instance.from_user = request.user
            form.save()
            return redirect('overview')
    else:
        form = TransactionForm()

    return render(request, 'bestbank/transfer.html', {'form': form})
