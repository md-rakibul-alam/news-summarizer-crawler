import requests
from bs4 import BeautifulSoup
from app.Summarizer.Summarizer import summarize_news

def scrape_news(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        div_content = soup.find_all('div', class_='story-element story-element-text')
        
        if div_content:
            all_text = ""
            for div in div_content:
                paragraphs = div.find_all('p')
                extracted_text = '\n'.join([p.get_text() for p in paragraphs])
                all_text += extracted_text
                all_text += '\n'
            
            summary = summarize_news(all_text)
            return summary
        else:
            return 'No content found'
    else:
        return 'Failed to retrieve the content'