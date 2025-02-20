import google.generativeai as genai
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env and .env.local files
load_dotenv()

# Configure the Gemini API
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def summarize_news(article_text: str):
    """
    Summarize a news article in its original language and provide English translation
    
    Args:
        article_text (str): The full text of the news article in any language
        
    Returns:
        dict: A dictionary containing both original and translated summaries
              in the format {"OriginalSummary": summary_text, 
                           "TranslatedSummary": english_summary}
    """
    
    prompt = """
    You are a skilled multilingual journalist. Analyze the following news article and provide two summaries:

    Requirements for Original Language Summary:
    1. Create a 90-word summary in the SAME LANGUAGE as the input article
    2. Keep it to a single paragraph
    3. Include the most important information
    4. Add analytical perspective while maintaining journalistic integrity
    5. Capture key events, people, and context

    Requirements for English Translation:
    1. Provide an accurate English translation of your original language summary
    2. Maintain the same meaning and tone
    3. Ensure natural English flow

    Please format your response in JSON format. The JSON will have two properties "OriginalSummary" and "TranslatedSummary".
    # Here is the JSOn format: {
        "OriginalSummary": "string",
        "TranslatedSummary": "string"
    }
    # Strictly follow the json format. It is very important for us.   
    # Don't add any extra information in the response except the json.
    # Output must be in JSON format.

    News Article:
    
    """
    model = genai.GenerativeModel("gemini-1.5-flash")  # Use latest model version
    response = model.generate_content(prompt + article_text)
    
    text = response.text.replace("```json\n", "").replace("```", "")
    response_dict = json.loads(text)

    return response_dict
