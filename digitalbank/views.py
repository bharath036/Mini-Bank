from django.shortcuts import render,redirect 
from .models import AddTransaction,CurrentBalance
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password=password)
        if user is None:
            messages.success(request,'Invali user or password incorrect')
            return redirect('login_view')
        
        login(request,user)
        return redirect('index')
    
    return render(request,'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.success(request,'Username already taken')
            return redirect('register_view')
        
        user = User.objects.create(
            username=username,
            password = password,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save()
        messages.success(request,'Account created')
        return redirect('login_view')
    return render(request,'register.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')
'''
def index(request):
    print("inside index.html")
    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        select_type = 'Credit'
        current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
        enter_amount = request.POST.get('amount')
        print(enter_amount)
        print(request.method)
        transaction_history = AddTransaction.objects.create(
            username = username,
            enter_amount = enter_amount,
            current_balance = current_balance,
            select_type = select_type
        )
        return redirect('/')
    current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
    return render(request,"index.html")
'''

@login_required(login_url="login_view")
def index(request):
    #print("inside index.html")
    if request.method == "POST":
        username = request.POST.get('username')
        #print(username)
        select_type = 'Credit'
        current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
        enter_amount = request.POST.get('amount')
        if float(enter_amount)< 0:
            select_type = 'Debit'
       # print(enter_amount)
       # print(request.method)
        transaction_history = AddTransaction.objects.create(
            username = username,
            enter_amount = enter_amount,
            current_balance = current_balance,
            select_type = select_type
        )
        current_balance.current_balance += float(transaction_history.enter_amount)
        current_balance.save()
       # print(current_balance.current_balance)
        return redirect('/')
    current_balance,_ = CurrentBalance.objects.get_or_create(id=1)
    #print(current_balance.current_balance)
    Credit = 0
    Debit = 0 

    for transaction_history in AddTransaction.objects.all():
        if transaction_history.select_type == 'Credit':
            Credit = Credit+ transaction_history.enter_amount
        else:
            Debit = Debit - transaction_history.enter_amount
    #this was passing to present in html so that users can view
    context = { 'Credit':Credit ,
               'Debit' : Debit,
                'transactions': AddTransaction.objects.all(),
                'current_balance': current_balance.current_balance
    }
    return render(request,"index.html",context)