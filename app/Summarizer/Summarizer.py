import google.generativeai as genai
import json
from dotenv import load_dotenv
import os
from pymongo import MongoClient

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

    ## Requirements for Original Language Summary:
    * Create a 90-word summary in the SAME LANGUAGE as the input article
    * Keep it to a single paragraph
    * Include the most important information
    * Add analytical perspective while maintaining journalistic integrity
    * Capture key events, people, and context
    * Write in complete sentences
    * The summary should be a maximum of 60 words.

    ## Requirements for Translated Summary:
    * Provide an accurate English translation of your original summary
    * Maintain the same meaning and tone as the original summary
    * Ensure natural English flow
    * Do not include any additional information rather than the original summary
    * Keep it to a single paragraph
    * Add analytical perspective while maintaining journalistic integrity
    * Write in complete sentences
    * The summary should be a maximum of 65 words.

    ## Requirements for OriginalTitle:
    * Go through the article and provide a title in the SAME LANGUAGE as the input article.
    * The title should be a maximum of 20 words.
    * The title should be catchy and informative.
    * The title should be in complete sentence format.
    * The title should be in the same language as the input article.

    ## Requirements for TranslatedTitle:
    * Provide an accurate English translation of your original title.
    * Maintain the same meaning and tone as the original title.
    * Ensure natural English flow.
    * The title should be a maximum of 20 words.

    ## Requirements for Category:
    * Provide the category of the news article.
    * The category should be a list of strings.
    * The category should be a maximum of 3 strings.
    * The category should be in English
    * Pick the category of the news article from the following list: ["Bangladesh", "Politics", "Business", "Technology", "Entertainment", "Sports", "Health", "Science", "International", "Fashion", "Education", "Health & Fitness"].
    * If the news article does not fit into any of the categories, please provide the most relevant category.
    * There should be at least one category.
    * There should be no duplicate categories.
    * Pick the most relevant category/categories.

    ## Requirements for Sentiment:
    * Analyze this news article and classify it as "Positive", "Negative", or "Neutral".
    * The sentiment should be in English.
    * The sentiment should be a single string.
    * The sentiment should be based on the overall tone of the news article.
    * The sentiment should be based on the content of the news article.

    ## Requirements for OriginalKeyPharases:
    * Extract key terms or phrases from the article.
    * Provide a list of keywords.
    * The keywords should be in the same language as the input article.
    * The keywords should be relevant to the content of the article.
    * The keywords should be a maximum of 10 words.

    ## Requirements for TranslatedKeyPharases:
    * Provide an accurate English translation of your original keywords.
    * Maintain the same meaning as the original keywords.
    * Ensure natural English flow.
    * The keywords should be relevant to the content of the article.
    * The keywords should be a maximum of 10 words.


    ## Here is the JSON format: 
    {
        "OriginalSummary": "string",
        "TranslatedSummary": "string",
        "OriginalTitle": "string",
        "TranslatedTitle": "string",
        "Category": ["string"],
        "Sentiment": "string",
        "OriginalKeyPharases": ["string"],
        "TranslatedKeyPharases": ["string"]
    }

    ## Strictly follow the json format. It is very important for us.   
    ## Don't add any extra information in the response except the json.
    ## Output must be in JSON format.

    News Article:
    
    """
    model = genai.GenerativeModel("gemini-1.5-flash")  # Use latest model version
    response = model.generate_content(prompt + article_text)
    
    text = response.text.replace("```json\n", "").replace("```", "")
    response_dict = json.loads(text)

    return response_dict
