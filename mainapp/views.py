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
        age = int(request.POST.get("age"))
        income = float(request.POST.get("income"))
        credit_score = float(request.POST.get("credit_score"))
        employment_status = int(request.POST.get("employment_status"))

        model_path = os.path.join(os.path.dirname(__file__), 'credit_model.pkl')
        model = joblib.load(model_path)

        prediction = model.predict([[age, income, credit_score, employment_status]])

        if prediction[0] == 1:
            return render(request, "mainapp/loan_success_new.html", {"message": "Loan Approved ✅"})
        else:
            return render(request, "mainapp/loan_success_new.html", {"message": "Loan Denied ❌"})

    return render(request, "mainapp/loan_form.html")

def loan_success(request):
    return render(request, "mainapp/loan_success_new.html")


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')
        else:
            return render(request, 'mainapp/register.html', {'error': 'Username already exists'})
    
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
            if model is not None:
                data = form.cleaned_data
                input_data = np.array([[data['monthly_income'], data['monthly_expenses'],
                                        data['num_employees'], data['years_in_business'],
                                        1 if data['defaulted_before'] == 'Yes' else 0]])

                pred = model.predict(input_data)[0]
                label = {0: "High Risk", 1: "Medium Risk", 2: "Low Risk"}
                prediction = label.get(pred, "Unknown")
            else:
                prediction = "⚠️ Model not found"
    else:
        form = LoanForm()

    return render(request, 'mainapp/dashboard.html', {'form': form, 'prediction': prediction})


def logout_view(request):
    logout(request)
    return redirect('login')
