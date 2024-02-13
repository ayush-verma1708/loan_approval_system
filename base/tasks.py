from celery import shared_task
import pandas as pd
from .models import Customer,Loan

@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"

@shared_task
def ingest_data_from_excel():
    try:
        #Read customer data from Excel
        customer_df = pd.read_excel('base/static/customer_data.xlsx')
        for _,row in customer_df.iterrows():
            Customer.objects.create(
                c_id=row['Customer ID'],
                f_name=row['First Name'],
                l_name=row['Last Name'],
                age = row['Age'],
                phone_number=row['Phone Number'],
                monthly_salary=row['Monthly Salary'],
                approved_limit=row['Approved Limit'],

            )
        loan_df = pd.read_excel('base/static/loan_data.xlsx')
        # Iterate over rows and create Loan objects
        for _, row in loan_df.iterrows():
            Loan.objects.create(
                c_id=row['Customer ID'],
                l_id=row['Loan ID'],
                loan_amount=row['Loan Amount'],
                tenure=row['Tenure'],
                interest_rate=row['Interest Rate'],
                monthly_payment=row['Monthly payment'],
                emi_on_time=row['EMIs paid on Time'],
                date_of_approval=row['Date of Approval'],
                end_date=row['End Date']
            )
    except Exception as e:
        print(f"Error occurred during data ingestion: {e}")    