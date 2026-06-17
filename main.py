from src.scraper import fetch_data

if __name__ == "__main__":
    print("جاري تشغيل نظام تحليل مشاعر السوق...")
    data = fetch_data()
    print(f"تم جلب البيانات بنجاح: {data}")
