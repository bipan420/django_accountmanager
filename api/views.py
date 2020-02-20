from rest_framework import mixins,generics
from .serializer import ExpensesSerializer
from expenses.models import Expenses

class ExpensesApiView(mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()

    #Displays the data read from the queryset on the list
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)