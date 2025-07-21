# mainapp/ml_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Train and save model
def train_model():
    # Dummy dataset - you can replace this later with a real CSV
    data = {
        'age': [25, 40, 35, 23, 45],
        'income': [50000, 80000, 60000, 40000, 100000],
        'credit_score': [650, 700, 620, 580, 750],
        'loan_approved': [1, 1, 0, 0, 1]  # 1 = approved, 0 = not approved
    }

    df = pd.DataFrame(data)
    X = df[['age', 'income', 'credit_score']]
    y = df['loan_approved']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Save model to a file
    model_path = os.path.join('mainapp', 'credit_model.pkl')
    joblib.dump(model, model_path)
    print("✅ Model trained and saved to:", model_path)
