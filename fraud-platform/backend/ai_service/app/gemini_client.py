import google.generativeai as genai
import os
from typing import Dict, Any


class GeminiClient:
    def __init__(self):
        # Configure Gemini API
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
    
    async def analyze_fraud(self, transaction_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze transaction data for potential fraud using Gemini AI"""
        if not self.model:
            return {
                "error": "Gemini API key not configured",
                "is_fraudulent": False,
                "confidence": 0.0
            }
        
        # Create prompt for fraud analysis
        prompt = f"""
        Analyze the following transaction for potential fraud:
        
        Transaction Details:
        {transaction_data}
        
        Provide a fraud risk assessment with:
        1. Whether this transaction appears fraudulent (yes/no)
        2. Confidence score (0-1)
        3. Explanation for your assessment
        
        Respond in JSON format.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return {
                "analysis": response.text,
                "transaction_id": transaction_data.get("transaction_id", "unknown")
            }
        except Exception as e:
            return {
                "error": str(e),
                "is_fraudulent": False,
                "confidence": 0.0
            }
