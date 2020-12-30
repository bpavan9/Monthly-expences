from django.shortcuts import render,redirect
from .models import Item,Wallet,Wallet_balance
from .forms import SinupForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.

def sinup(request):
    form=SinupForm(request.POST or None)
    context={'form':form}
    if request.method =="POST":
        if form.is_valid():
            form.save()
            username = form.changed_data.get('username')
            password = form.changed_data.get('password')
            # login(request.user)
            return redirect('monthlyexp/profile')
    return render(request,'monthlyexp/sinup.html',context)




@login_required(login_url='/monthlyexp/login')
def home(request):
    total_expences=0
    items = Item.objects.all()
    if request.method == "GET":
        for item in items:
            total_expences +=item.price
            context = {
                'total_expences':total_expences,
                'items':items,
                }
    return render(request,'monthlyexp/profile.html',context)


def transaction(request):
    total_balance=0
    wallets = Wallet.objects.all()
    if request.method == "GET":
        for wallet in wallets:
            total_balance +=wallet.credit_amount
            total_balance -=wallet.debit_amount
            context={
                'total_balance':total_balance,
                'wallets':wallets,
            }
    return render(request, 'monthlyexp/balance.html',context)


def expence(request):
    total_expamount=0
    wallet_funds=0
    wallet_balances=Wallet_balance.objects.all()
    if request.method == "GET":
        for wallet_balance in wallet_balances:
            total_expamount += wallet_balance.purchaseiteam_price
            wallet_funds += wallet_balance.wallet_credit_amount
            wallet_funds -= wallet_balance.wallet_debit_amount
            context={
                "total_expamount":total_expamount,
                "wallet_funds":wallet_funds,
                "wallet_balances":wallet_balances,
            }
    return render(request,'monthlyexp/new.html',context)
















