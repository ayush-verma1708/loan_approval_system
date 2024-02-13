from rest_framework import serializers
from .models import Customer,Loan

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['c_id','f_name','l_name','age','phone_number','monthly_salary','approved_limit']
