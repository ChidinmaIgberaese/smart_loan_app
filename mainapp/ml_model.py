import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Path to save the trained model 
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'credit_model.pkl')

def train_model():
    data = {
        'age': [25, 45, 35, 52, 23],
        'income': [30000, 80000, 50000, 120000, 25000],
        'expenses': [2000, 3000, 2500, 4000, 1500],
        'loan_amount': [10000, 20000, 15000, 30000, 5000],
        'repayment_duration': [12, 24, 18, 24, 6],
        'guarantor': [1, 0, 1, 1, 0],
        'employment_status': [1, 2, 1, 0, 1],
        'credit_score': [700, 650, 720, 680, 600],
        'target': [1, 0, 1, 1, 0]
    }
    
    df = pd.DataFrame(data)
    
    X = df[['age', 'income', 'expenses', 'loan_amount', 'repayment_duration', 'guarantor', 'employment_status', 'credit_score']]
    y = df['target']
    
    model = LogisticRegression()
    model.fit(X, y)
    
    joblib.dump(model, MODEL_PATH)
    print(f"Model retrained and saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_model()
