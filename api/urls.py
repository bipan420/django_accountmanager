from django.urls import path
from .views import ExpensesApiView
urlpatterns = [
    path('expenses/',ExpensesApiView.as_view())
]
