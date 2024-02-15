from django.shortcuts import render, redirect
from django.http import HttpResponse
from .tasks import ingest_data_from_excel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Loan
from .serializer import CustomerSerializer
from .forms import userRegisterForm
from datetime import datetime
from django.db.models import Sum

def test(request):
    ingest_data_from_excel.delay()
    return HttpResponse("Done")

@api_view(['POST'])
def register_customer(request):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            return Response({
                'customer_id': customer.c_id,
                'name': f'{customer.f_name} {customer.l_name}',
                'age': customer.age,
                'phone_number': customer.phone_number,
                'monthly_salary': customer.monthly_salary,
                'approved_limit': customer.approved_limit,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def register_form(request):
    if request.method =="POST":
        form = userRegisterForm(request.POST)
        if form.is_valid():
            new_customer = form.save()
            return redirect('user_response', pk=new_customer.pk)    
    else:
        form = userRegisterForm()
        
    context = {'form':form}    
    return render(request,'index.html',context)

def user_page(request):
    customer = Customer.objects.all()
    return render(request,'user.html',{'customer':customer})

def user_response_page(request,pk):
    customer = Customer.objects.get(pk=pk)
    loans = Loan.objects.filter(c_id = pk)
    context = {'customer':customer,'loans':loans}
    return render(request, 'user_response.html', context)

def delete_all(request):
    Customer.objects.all().delete()
    Loan.objects.all().delete()
    return render(request, 'user.html')


def check_eligibility(request):
    return render(request, 'user.html')