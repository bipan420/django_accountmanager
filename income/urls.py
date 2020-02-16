from django.urls import path
from .views import IncomeCategoryView,AddIncomeView,AllIncomeView,editIncome,deleteIncome

urlpatterns = [
    path('category/',IncomeCategoryView.as_view(),name='income_category'),
    path('create/',AddIncomeView.as_view(),name='add_income'),
    path('',AllIncomeView.as_view(),name='all_income'),
    path('edit/<int:id>',editIncome,name='edit_income'),
    path('delete/<int:id>',deleteIncome,name='delete_income')
    
]
