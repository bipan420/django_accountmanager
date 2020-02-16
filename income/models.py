from django.db import models
from abstract.models import Category,Abs
from django.db.models import Sum
import datetime
from datetime import timedelta

# Create your models here.

class IncomeCategory(Category):

    class Meta:
        db_table = 'income_category'

    def __str__(self):
        return self.title
    



class IncomeManager(models.Manager):
    def getIncomeOfToday(self,user_id):
        return self.filter(user_id = user_id,
        date = datetime.date.today()).aggregate(Sum('amount'))
    
    def getIncomeOfMonth(self,user_id):
        return self.filter(user_id = user_id,
        date_month = datetime.date.today().month,
        date_year = datetiem.date.today().year).aggregate(Sum('amount'))

    def getIncomeOfPreviousMonth(self,user_id):
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year
        if current_month-1 == 0:
            previous_month = 12
            previous_year = current_year-1
        else:
            previous_month = current_month-1
            previous_year = current_year
        return self.filter(user_id=user_id,
                        date_month = previous_month,
                        date_year = previous_year).aggregate(Sum('amount'))
    
    def getIncomeOfYesterday(self,user_id):
        yesterday = datetime.date.today() - timedelta(days=1)
        return self.filter(user_id=user_id,
                            date = yesterday).aggregate(Sum('amount'))
    
    def getIncomeByCategory(self,user_id):
        category = Income.objects.filter(user_id = user_id)
        allbycategory = {}
        for c in category:
            i = IncomeCategory.objects.filter(user_id=user_id, category=c).aggregate(Sum('amount'))
            allbycategory[c.title] = i['amount__sum']
        return allbycategory

            



class Income(Abs):
    image = models.ImageField(upload_to='income/',blank=True,null=True,)
    category = models.ForeignKey(IncomeCategory,on_delete=models.CASCADE)
    objects = IncomeManager()
    class Meta:
        db_table = 'income'

    def __str__(self):
        return self.title


