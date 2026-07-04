from src.scraper import fetch_financial_news
from src.analyzer import analyze_sentiment

if __name__ == "__main__":
    print("=== جاري سحب الأخبار الحية والواقعية الآن... ===")

    news = fetch_financial_news()

    if news:
        print("\n=== نتائج سحب الأخبار وتحليل المشاعر بالذكاء الاصطناعي===")
        for index, headline in enumerate(news, 1):
            label, score = analyze_sentiment(headline)


            print(f"{index}. 📰 الخبر: {headline}")
            print(f"   📊 التحليل: {label} (الدرجة: {score})")
            print("-" * 60)  # خط فاصل بين كل خبر وخبر
    else:
        print("لم يتم العثور على أخبار، تأكدي من الكود أو الموقع.")
