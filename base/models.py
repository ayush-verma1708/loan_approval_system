from django.db import models

# Create your models here.
class Customer(models.Model):   
    c_id = models.AutoField(primary_key=True, editable=False)
    f_name = models.CharField(max_length= 255)
    l_name = models.CharField(max_length= 255)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=255)
    monthly_salary = models.BigIntegerField()
    approved_limit = models.BigIntegerField()


    def __str__(self):
        return f'C_ID : {self.c_id}'
    
class Loan(models.Model):
    # c_id = models.ForeignKey(Customer, related_name='loans', on_delete=models.CASCADE, null=True)
    id = models.AutoField(primary_key=True)
    c_id = models.IntegerField(null=True)
    l_id = models.IntegerField()
    loan_amount = models.BigIntegerField()
    tenure = models.IntegerField()
    interest_rate = models.IntegerField(null=True)
    monthly_payment = models.IntegerField()
    emi_on_time = models.IntegerField()
    date_of_approval = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'Loan ID {self.l_id} Customer ID {self.c_id}'