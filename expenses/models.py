from django.db import models
from abstract.models import Category,Abs

# Create your models here.

class ExpensesCategory(Category):

    class Meta:
        db_table = 'expenses_category'

    def __str__(self):
        return self.title

        

class Expenses(Abs):
    image = models.ImageField(upload_to='expenses/',blank=True,null=True)
    category = models.ForeignKey(ExpensesCategory,on_delete=models.CASCADE)

    class Meta:
        db_table = 'expenses'

    def __str__(self):
        return self.title
    
    