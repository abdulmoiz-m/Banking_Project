from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


# @login_required(login_url='login')
# balance and transactions
def overview(request):
    return render(request, 'overview.html')
