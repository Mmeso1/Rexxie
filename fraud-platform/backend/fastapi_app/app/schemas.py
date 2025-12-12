from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Transaction(BaseModel):
    transaction_id: str
    amount: float
    timestamp: datetime
    merchant_id: str
    user_id: str
    location: Optional[str] = None


class FraudPrediction(BaseModel):
    transaction_id: str
    is_fraudulent: bool
    confidence_score: float
    explanation: Optional[str] = None
