from django import forms
from .models import Customer

class userRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = ['f_name', 'l_name', 'age', 'phone_number', 'monthly_salary', 'approved_limit']
        exclude = ('c_id', 'approved_limit')  # Exclude c_id and approved_limit from the form fields

    def save(self, commit=True):
        instance = super(userRegisterForm, self).save(commit=False)

        last_c_id = Customer.objects.last().c_id if Customer.objects.exists() else 0
        instance.c_id = max(last_c_id + 1, 301)

        monthly_salary = instance.monthly_salary
        instance.approved_limit = round(36 * monthly_salary, -5)

        if commit:
            instance.save()
        return instance