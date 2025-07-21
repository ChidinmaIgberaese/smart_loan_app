from django.db import models
from django.contrib.auth.models import User
import os
import joblib
from django.conf import settings

class UserProfile(models.Model):
    """Extends Django User model with extra fields (optional)"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    approval_status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.user.username

class CreditScore(models.Model):
    """Stores credit score predictions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()
    risk_level = models.CharField(max_length=20)  # e.g. Low, Medium, High
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"


def load_model():
    model_path = os.path.join(settings.BASE_DIR, 'model.pkl')
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        return None  
