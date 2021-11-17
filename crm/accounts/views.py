from django.shortcuts import render,redirect
from django.http import HttpResponse
from accounts.models import *
from accounts.forms import OrderForm
from .filters import OrderFilter
def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    totalorder=Order.objects.all().count()
    delivered=Order.objects.filter(status='Delivery').count()
    pending=Order.objects.filter(status='pending').count()
    context={'customers':customers,'orders':orders,
                'totalorder':totalorder,'delivered':delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)
def products(request):
    return render(request,'accounts/products.html')
def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    order=customer.order_set.all()
    totalorder=order.count()

    myfilter=OrderFilter(request.GET,queryset=order)
    order=myfilter.qs
    


    context={'order':order,'customer':customer,'pk':pk,'totalorder':totalorder,'myfilter':myfilter}
    return render(request,'accounts/customer.html',context)

def createorder(request,pk):
    customer=Customer.objects.get(id=pk)
    form=OrderForm(initial={'customer':customer})
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form,'customer':customer}
    return render(request,'accounts/formorder.html',context)

def updateorder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form,}
    return render(request,'accounts/formorder.html',context)

def deleteorder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request,'accounts/deleteorder.html',context)
