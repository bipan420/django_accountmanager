from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unique_together = ('title','user_id')

    def __str__(self):
        return self.title
    


class Abs(models.Model):
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.TextField(blank=True,null=True)
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        abstract = True