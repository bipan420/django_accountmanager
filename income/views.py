from django.shortcuts import render,redirect
from django.views import View
from .forms import IncomeCategoryForm,IncomeForm
from django.contrib import messages
from .models import IncomeCategory,Income



# Create your views here.


class IncomeCategoryView(View):
    template_name = 'income_category.html'
    def get(self,request):
        context = {
            'form':IncomeCategoryForm,
            'category':IncomeCategory.objects.filter(user_id=request.user.id)
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = IncomeCategoryForm(request.POST)
        if form.is_valid():
            #Don't commit without adding the user_id
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request,messages.SUCCESS,'Data Added Successfully')
            return redirect('income_category')
        else:
            messages.add_message(request,messages.ERROR,'Sorry data cannot be added')
            return redirect('income_category')


class AddIncomeView(View):
    template_name = 'add_income.html'
    def get(self, request):
        context = {
            'form':IncomeForm
        }
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form = IncomeForm(request.POST,request.FILES or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            messages.add_message(request,messages.SUCCESS,'Data Added Successfully')
            return redirect('add_income')
        else:
            messages.add_message(request,messages.ERROR,'Sorry data cannot be added')
            return redirect('add_income')


class AllIncomeView(View):
    template_name = 'income.html'
    def get(self,request):
        context = {
            'all': Income.objects.filter(user_id = request.user.id)
        }
        return render(request,self.template_name,context)

def editIncome(request,id):
    form = IncomeForm(request.POST or None,request.FILES or None,instance=Income.objects.get(id=id))
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,'Successfully updated')
        return redirect('all_income')
    return render(request,'edit_income.html',context = {'form':form})


def deleteIncome(request,id):
    a = Income.objects.get(id=id)
    a.delete()
    messages.add_message(request,messages.SUCCESS,'Successfully deleted')
    return redirect('all_income')