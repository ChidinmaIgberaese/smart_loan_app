import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Path to save the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'credit_model.pkl')

def train_model():
    # ✅ Dummy dataset
    data = {
        'age': [25, 45, 35, 52, 23, 43, 36, 29],
        'income': [30000, 80000, 50000, 120000, 25000, 70000, 60000, 40000],
        'loan_amount': [10000, 20000, 15000, 30000, 5000, 18000, 16000, 9000],
        'credit_score': [0, 1, 1, 1, 0, 1, 1, 0]  # 1 = Good credit, 0 = Bad credit
    }
    
    df = pd.DataFrame(data)
    
    X = df[['age', 'income', 'loan_amount']]
    y = df['credit_score']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, MODEL_PATH)
    print(f"✅ Model trained and saved to {MODEL_PATH}")
