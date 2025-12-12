from fastapi import FastAPI
from .gemini_client import GeminiClient

app = FastAPI()
gemini_client = GeminiClient()


@app.get("/")
async def root():
    return {"message": "AI Service for Fraud Detection"}


@app.post("/analyze")
async def analyze_transaction(transaction_data: dict):
    """Analyze transaction for fraud using Gemini AI"""
    result = await gemini_client.analyze_fraud(transaction_data)
    return result
