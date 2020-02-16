from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from expenses.models import Expenses
from income.models import Income

class SignupView(View):
    template_name = 'signup.html'

    def get(self,request):
        return render(request,self.template_name)
    
    def post(self,request,*args,**kwargs):
        f = request.POST.get('fname')
        l = request.POST.get('lname')
        e = request.POST.get('email')
        u = request.POST.get('username')
        p1 = request.POST.get('pass1')
        p2 = request.POST.get('pass2')

        if p1==p2:
            try:
                u = User(username=u,email=e,first_name=f,last_name=l)
                u.set_password(p1)
                u.save()
                messages.add_message(request,messages.SUCCESS,'Signup successful')
                return redirect('login')
            except:
                messages.add_message(request,messages.ERROR,'Username already exists')
                return redirect('signup')
        else:
            messages.add_message(request,messages.ERROR,'Password does not match')
            return redirect('signup')




class LoginView(View):
    template_name = 'login.html'

    def get(self,request):
        
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username = u,password = p)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.add_message(request,messages.ERROR,'Username or password does not match')
            return redirect(login)



class DashboardView(LoginRequiredMixin,View):
    login_url = '/login'
    template_name = 'dashboard.html'

    def get(self,request):
        context = {
            'exp': Expenses.objects.getExpensesOfToday(request.user.id),
            'income': Income.objects.getIncomeOfToday(request.user.id),

        }
        return render(request,self.template_name,context)


def signout(request):
    logout(request)
    return redirect('login')

