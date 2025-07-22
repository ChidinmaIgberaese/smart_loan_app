# CrediScope AI - Loan Application System

CrediScope AI is a Django-based web application designed to simplify and automate the loan application process. Users can register, log in, apply for loans, and track their application status via a simple dashboard. It also predicts creditworthiness using a trained machine learning model and provides financial visualizations.

## Features

- ✅ User registration and login
- ✅ Secure authentication system
- ✅ Submit loan applications
- ✅ Personalized dashboard to view application status and credit score
- ✅ Credit score prediction using AI (Low / Medium / High)
- ✅ Data visualization with Chart.js
- ✅ Success confirmation screen
- 🚧 Admin review functionality (optional future feature)

## Folder Structure

```
CrediScopeAI/
│
├── backend/
│   ├── crediscope/          # Django project config
│   ├── predictor/           # Django app with views, models, forms
│   ├── model.pkl            # Trained ML model for credit prediction
│   └── templates/           # HTML templates
│       ├── register.html
│       ├── login.html
│       ├── dashboard.html
│       └── loan_form.html
│
├── static/
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files (e.g., Chart.js)
│   └── images/              # Branding assets
│
├── dataset/
│   └── dummy_credit_data.csv  # Sample data for model training
│
├── model_training/
│   └── train_model.ipynb      # Notebook for training and exporting model.pkl
│
└── README.md
```

## Tech Stack

| Layer            | Tools Used                                |
| ---------------- | ----------------------------------------- |
| Frontend         | HTML, CSS, JavaScript, Chart.js           |
| Backend          | Django (Python)                           |
| Machine Learning | scikit-learn, pandas                      |
| Database         | SQLite (development), PostgreSQL (Render) |
| Hosting          | Render                                    |

## How It Works

1. Users register/login using Django authentication.
2. They input financial info (income, expenses, etc.).
3. Data is passed to the `model.pkl` to predict credit score.
4. Result is visualized with Chart.js on the dashboard.
5. (Optional) Admin can review or approve loan applications.

## ✅ Your Model's Inputs (features):

These are the variables your model looks at to decide someone's credit risk:

Loan Amount

Loan Term (in months)

Credit Score

Income

Employment Status (e.g. employed, self-employed, unemployed)

Purpose of Loan (e.g. education, business, medical, etc.)

Age

Gender

## 📊 Credit Risk Qualification Criteria (Model Explanation)

Note: These are not hard-coded rules but patterns learned from the training data. The model evaluates combinations of features to make a decision.

## 🟢 Qualified Applicant (Low Risk)

A user is likely to qualify for a loan if they meet the following:

Earn ₦500,000 or more per month

Have a credit score above 700

Request a loan that is not more than 40% of their income

Have been employed for over 2 years

Are between 25 and 50 years old

Choose a productive loan purpose (e.g., business, education)

Have a debt-to-income ratio below 35%

Maintain a healthy savings balance

These indicators suggest financial stability, so the model predicts them as Low Risk, meaning they're likely to be approved

## 🔍 Example Logic (How Model Might Interpret):

A user earning ₦700,000/month requesting ₦150,000 with a credit score of 720 and over 3 years of employment history would likely be Low Risk.

A user earning ₦100,000/month requesting ₦500,000 with a low credit score and short job history would likely be High Risk.

Built by Chidinma Igberaese for CODEHER Hackathon Powerlearnprojectafrica  
Inspired by real challenges faced by Nigerian youth and micro-entrepreneurs.

CrediScopeAI/
│
├── backend/
│ ├── crediscope/ # Django project config
│ ├── predictor/ # Django app with views, models, forms
│ ├── model.pkl # Trained ML model for credit prediction
│ └── templates/ # HTML templates
│ ├── register.html
│ ├── login.html
│ ├── dashboard.html
│ └── loan_form.html
│
├── static/
│ ├── css/ # Stylesheets
│ ├── js/ # JavaScript files (e.g., Chart.js)
│ └── images/ # Branding assets
│
├── dataset/
│ └── dummy_credit_data.csv # Sample data for model training
│
├── model_training/
│ └── train_model.ipynb # Notebook for training and exporting model.pkl
│
└── README.md
