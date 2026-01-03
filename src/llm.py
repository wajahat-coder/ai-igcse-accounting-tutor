import os
from typing import Optional

class LLMClient:
    """OpenAI LLM adapter for IGCSE Accounting Tutor."""
    
    def __init__(self):
        """Initialize LLM client with OpenAI API key from environment."""
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.available = bool(self.api_key)
    
    def answer(self, prompt: str, max_tokens: int = 256) -> str:
        """
        Get answer from OpenAI API.
        
        Args:
            prompt: Question/prompt for the model
            max_tokens: Maximum tokens in response (default 256)
        
        Returns:
            Answer from OpenAI or fallback message if key unavailable
        """
        if not self.available:
            return "OpenAI API key not configured. Using fallback answers."
        
        try:
            import openai
            openai.api_key = self.api_key
            
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error querying OpenAI: {str(e)}"
