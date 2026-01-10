from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'balance', 'created_at']
    list_filter = ['created_at']
    search_fields = ['username', 'email']
