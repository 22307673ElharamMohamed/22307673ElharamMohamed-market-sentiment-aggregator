import requests
from bs4 import BeautifulSoup

def fetch_financial_news():
    url = "https://finance.yahoo.com/news/"
   response =  requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    for item in soup.find_all('h3', limit=10):
         title = item.get_text(strip=True)
         headlines.append(title)
   
    return headlines 


else:
    print("connection faild")
    return[]
    
    

    
