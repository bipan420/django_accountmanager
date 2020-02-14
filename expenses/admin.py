from django.contrib import admin
from .models import ExpensesCategory,Expenses

# Register your models here.
admin.site.register(ExpensesCategory)
admin.site.register(Expenses)