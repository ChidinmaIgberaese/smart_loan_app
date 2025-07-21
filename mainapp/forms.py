# mainapp/forms.py
from django import forms

class LoanForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=18)
    monthly_income = forms.FloatField(min_value=0)
    monthly_expenses = forms.FloatField(min_value=0)
    loan_amount = forms.FloatField(min_value=0)
    repayment_duration = forms.ChoiceField(choices=[
        ('6_months', '6 Months'),
        ('12_months', '1 Year'),
        ('18_months', '1.5 Years'),
        ('24_months', '2 Years'),
    ])
    guarantor_available = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')])
    employment_status = forms.ChoiceField(choices=[
        ('employed', 'Employed'),
        ('self-employed', 'Self-Employed'),
        ('unemployed', 'Unemployed'),
    ])
    business_type = forms.CharField(max_length=100, required=False)
    loan_purpose = forms.CharField(max_length=200)

    # credit_score = forms.FloatField(required=False, min_value=0)
