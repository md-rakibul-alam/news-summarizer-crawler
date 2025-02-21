import requests
from bs4 import BeautifulSoup
from app.Summarizer.Summarizer import summarize_news
from app.DatabaseContext.DatabaseContext import DatabaseContext
from uuid import uuid4

class ContentScrapper:
    def __init__(self, db_context: DatabaseContext):
        self.db_context = db_context

    def scrape_news(self, url):
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

                news_content = {
                    'Id': str(uuid4()),
                    'Url': url,
                    "ArticleText": all_text,
                    "OriginalSummary": summary["OriginalSummary"],
                    "TranslatedSummary": summary["TranslatedSummary"],
                    "OriginalTitle": summary["OriginalTitle"],
                    "TranslatedTitle": summary["TranslatedTitle"],
                    "Category": summary["Category"]
                }
                
                # Use DatabaseContext to save the news content
                self.db_context.SaveNews(news_content)
                
                return summary
            else:
                return 'No content found'
        else:
            return 'Failed to retrieve the content'

# Example usage
if __name__ == "__main__":
    db_context = DatabaseContext()
    scrapper = ContentScrapper(db_context)
    url = "http://example.com/news-article"
    print(scrapper.scrape_news(url))