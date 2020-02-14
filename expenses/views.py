from django.shortcuts import render,redirect
from django.views import View
from .forms import ExpensesCategoryForm,ExpensesForm
from django.contrib import messages
from .models import ExpensesCategory,Expenses
# Create your views here.

class ExpensesCategoryView(View):
    template_name = 'expenses_category.html'
    def get(self,request):
        context = {
            'form': ExpensesCategoryForm(),
            'category': ExpensesCategory.objects.filter(user_id=request.user.id)
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = ExpensesCategoryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request,messages.SUCCESS,'Successfully added')
            return redirect('expenses_category')
        else:
            messages.add_message(request,messages.ERROR,'Sorry your request cannot be added')
            return redirect('expenses_category')
    

class AddExpensesView(View):
    template_name = 'add_expenses.html'
    def get(self,request):
        context = {
            'form':ExpensesForm
        }
        return render(request,self.template_name,context)


    def post(self,request,*args,**kwargs):
        form = ExpensesForm(request.POST,request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request,messages.SUCCESS,'Successfully added')
            return redirect('add_expenses')
        else:
            messages.add_message(request,messages.ERROR,'Sorry your request cannot be added')
            return redirect('add_expenses')


class AllExpensesView(View):
    template_name = 'expenses.html'

    def get(self,request):
        context={
            'all': Expenses.objects.filter(user_id=request.user.id)
        }
        return render(request,self.template_name,context)


def editExpenses(request,slug):
    form = ExpensesForm(request.POST or None, request.FILES or None,instance=Expenses.objects.get(id=id))
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,"Successfully updated")
        return redirect('all_expenses')
    return render(request,'edit_expenses.html',context={'form':form})

def deleteExpenses(request,id):
    a = Expenses.objects.get(id=id)
    a.delete()
    messages.add_message(request,messages.SUCCESS,'Dleted Succesfully')
    return redirect('all_expenses')
