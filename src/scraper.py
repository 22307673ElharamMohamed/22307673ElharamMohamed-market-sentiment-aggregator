import requests
from bs4 import BeautifulSoup


def fetch_financial_news():
    url = "https://finance.yahoo.com/news/"

    # بطاقة الهوية المزيفة عشان نخدع ياهو فاينانس 😎
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # نمرر الـ headers مع الطلب هنا
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = []
        for item in soup.find_all('h3', limit=10):
            title = item.get_text(strip=True)
            headlines.append(title)

        return headlines
    else:
        # بنخليه يطبع الكود عشان نعرف وش المشكلة بالضبط لو رفض
        print(f"فشل الاتصال بالموقع! رمز الاستجابة: {response.status_code}")
        return []
