from django.shortcuts import render,redirect 
from .models import AddTransaction,CurrentBalance

# Create your views here.
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