from src.scraper import fetch_financial_news

if __name__ == "__main__":
    print("=== جاري سحب الأخبار الحية والواقعية الآن... ===")

    news = fetch_financial_news()

    if news:
        for index, headline in enumerate(news, 1):
            print(f"{index}. {headline}")
    else:
        print("لم يتم العثور على أخبار، تأكدي من الكود أو الموقع.")
