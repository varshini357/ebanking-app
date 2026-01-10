from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def transfer(request):
    return render(request, 'payments/transfer.html')
