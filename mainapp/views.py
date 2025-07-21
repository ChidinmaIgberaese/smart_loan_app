from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import LoanForm

import joblib
import numpy as np
import os

# Load model once globally
model_path = os.path.join(settings.BASE_DIR, 'mainapp', 'credit_model.pkl')
model = joblib.load(model_path) if os.path.exists(model_path) else None


def home_view(request):
    return render(request, "mainapp/home.html")


def apply_loan(request):
    if request.method == "POST":
        # Extract form data from the request POST dictionary
        age = int(request.POST.get("age"))
        income = float(request.POST.get("income"))
        expenses = float(request.POST.get("monthly_expenses"))
        loan_amount = float(request.POST.get("loan_amount"))
        repayment_duration = request.POST.get("repayment_duration")  # map this to int months
        guarantor_available = request.POST.get("guarantor_available")
        employment_status = request.POST.get("employment_status")
        business_type = request.POST.get("business_type", "")  # Optional string
        loan_purpose = request.POST.get("loan_purpose", "")    # Optional string
        credit_score = request.POST.get("credit_score")

        # Convert repayment_duration to integer number of months
        repayment_map = {
            "6_months": 6,
            "12_months": 12,
            "18_months": 18,
            "24_months": 24,
        }
        repayment_duration_int = repayment_map.get(repayment_duration, 12)  # Default to 12 months

        # Mapping employment_status to integer expected by model
        employment_map = {"employed": 1, "self-employed": 2, "unemployed": 0}
        employment_int = employment_map.get(employment_status.lower(), 0)

        # Mapping guarantor_available to boolean/int
        guarantor_int = 1 if guarantor_available.lower() == "yes" else 0

        # Converting credit_score to float, default 0 if empty
        try:
            credit_score_float = float(credit_score)
        except (TypeError, ValueError):
            credit_score_float = 0.0

        # Preparing input array for model in correct order
        # **IMPORTANT**: The order here must match the order your model expects
        input_features = np.array([[
            age,
            income,
            expenses,
            loan_amount,
            repayment_duration_int,
            guarantor_int,
            employment_int,
            credit_score_float
        
        ]])

        # Run prediction
        prediction = model.predict(input_features)

        # Interpret prediction result (adjust based on your model's output scheme)
        if prediction[0] == 1:
            message = "Loan Approved ✅"
        else:
            message = "Loan Denied ❌"

        return render(request, "mainapp/loan_success_new.html", {"message": message})

    # If GET, just render the form
    return render(request, "mainapp/loan_form.html")


def loan_success(request):
    return render(request, "mainapp/loan_success_new.html")


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'mainapp/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'mainapp/register.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, email=email, password=password1)
        return redirect('login')

    return render(request, 'mainapp/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'mainapp/login.html', {'error': 'Invalid credentials'})

    return render(request, 'mainapp/login.html')

@login_required
def dashboard(request):
    prediction = None
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Numeric inputs
            monthly_income = data['monthly_income']
            monthly_expenses = data['monthly_expenses']
            loan_amount = data['loan_amount']
            age = data['age']

            # Encode repayment_duration
            repayment_map = {
                '6_months': 6,
                '12_months': 12,
                '18_months': 18,
                '24_months': 24
            }
            repayment_duration = repayment_map.get(data['repayment_duration'], 0)

            # Encode guarantor_available
            guarantor_available = 1 if data['guarantor_available'] == 'yes' else 0

            # Encode employment_status
            employment_map = {
                'employed': 0,
                'self-employed': 1,
                'unemployed': 2
            }
            employment_status = employment_map.get(data['employment_status'], 0)

            # Encode business_type as binary
            business_type = 1 if data['business_type'] else 0

            # Build feature array for model
            input_features = np.array([[
                monthly_income,
                monthly_expenses,
                loan_amount,
                repayment_duration,
                guarantor_available,
                employment_status,
                age,
                business_type
            ]])

            # Check for NaN (optional)
            if np.isnan(input_features).any():
                prediction = "⚠️ Invalid input: missing values detected"
            else:
                pred = model.predict(input_features)[0]
                label = {0: "High Risk", 1: "Medium Risk", 2: "Low Risk"}
                prediction = label.get(pred, "Unknown")

        else:
            prediction = "⚠️ Invalid form data"

    else:
        form = LoanForm()

    return render(request, 'mainapp/dashboard.html', {'form': form, 'prediction': prediction})

def logout_view(request):
    logout(request)
    return redirect('login')
