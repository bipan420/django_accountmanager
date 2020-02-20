from rest_framework import serializers
from expenses.models import Expenses

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id','title','date','amount','description','category']