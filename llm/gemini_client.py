import os
import google.generativeai as genai

def call_llm(system_prompt: str, user_prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY missing in .env")

    genai.configure(api_key=api_key)
    
    # gemini-flash-latest should point to the current stable flash model
    model = genai.GenerativeModel('gemini-flash-latest')

    combined_prompt = f"System Instruction: {system_prompt}\n\nUser Task: {user_prompt}"
    
    try:
        response = model.generate_content(combined_prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini: {str(e)}"
