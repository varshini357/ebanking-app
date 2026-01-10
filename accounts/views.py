from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Account
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            account = Account.objects.get(username=username)
            if account and password == 'demo123':  # Demo password
                # Create Django user session
                request.session['account_id'] = account.id
                request.session['username'] = account.username
                messages.success(request, f'Welcome back {account.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials')
        except Account.DoesNotExist:
            messages.error(request, 'Account not found')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard(request):
    account_id = request.session.get('account_id')
    account = Account.objects.get(id=account_id)
    return render(request, 'accounts/dashboard.html', {'account': account})

def logout_view(request):
    request.session.flush()
    return redirect('login')
