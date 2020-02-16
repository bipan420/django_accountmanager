from django.db import models
from abstract.models import Category,Abs
from django.db.models import Sum
import datetime
from datetime import timedelta

# Create your models here.

class ExpensesCategory(Category):

    class Meta:
        db_table = 'expenses_category'

    def __str__(self):
        return self.title


class ExpensesManager(models.Manager):
    def getExpensesOfToday(self,user_id):
        return self.filter(user_id = user_id,
        date=datetime.date.today()).aggregate(Sum('amount'))
    
    def getExpensesOfMonth(self,user_id):
        return self.filter(user_id = user_id,
        date_month = datetime.date.today().month,
        date_year = datetime.date.today().year).aggregate(Sum('amount'))

    def getExpensesOfPreviousMOnth(self,user_id):
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        if current_month-1 == 0:
            previous_month = 12
            previous_year = current_year-1
        else:
            previous_month = current_month-1
            previous_year = current_year

        return self.filter(user_id = user_id,
                        date_month = previous_month,
                        date_year=previous_year).aggregate(Sum('amount'))
    
    def getExpensesOfYesterday(self,user_id):
        yesterday = datetime.date.today()-timedelta(days=1)
        return self.filter(user_id = user_id,
                        date = yesterday).aggregate(Sum('amount'))

    def getExpensesByCategory(self,user_id):
        category = ExpensesCategory.objects.filter(user_id=user_id)
        allbycategory = {}
        for c in category:
            e = Expenses.objects.filter(user_id=user_id,category = c).aggregate(Sum('amount'))
            allbycategory[c.title] = e['amount__sum']
        return allbycategory


    





class Expenses(Abs):
    image = models.ImageField(upload_to='expenses/',blank=True,null=True)
    category = models.ForeignKey(ExpensesCategory,on_delete=models.CASCADE)

    objects = ExpensesManager()
    class Meta:
        db_table = 'expenses'

    def __str__(self):
        return self.title
    
    