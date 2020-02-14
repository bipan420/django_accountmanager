from django.db import models
from abstract.models import Category,Abs

# Create your models here.

class IncomeCategory(Category):

    class Meta:
        db_table = 'income_category'

    def __str__(self):
        return self.title
    


class Income(Abs):
    image = models.ImageField(upload_to='income/',blank=True,null=True,)
    category = models.ForeignKey(IncomeCategory,on_delete=models.CASCADE)

    class Meta:
        db_table = 'income'

    def __str__(self):
        return self.title