from django import forms

class LoanForm(forms.Form):
    monthly_income = forms.IntegerField()
    monthly_expenses = forms.IntegerField()
    num_employees = forms.IntegerField()
    years_in_business = forms.IntegerField()
    defaulted_before = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
