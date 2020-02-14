from django.urls import path
from .views import ExpensesCategoryView,AddExpensesView,AllExpensesView,editExpenses,deleteExpenses

urlpatterns = [
    path('category/',ExpensesCategoryView.as_view(),name='expenses_category'),
    path('create/',AddExpensesView.as_view(),name='add_expenses'),
    path('',AllExpensesView.as_view(),name='all_expenses'),
    path('edit/<int:id>',editExpenses,name='edit_expenses'),
    path('delete/<int:id>',deleteExpenses,name='delete_expenses')
]
