# 📈 Market Sentiment Aggregator

مشروع ذكي يقوم بسحب الأخبار المالية الحية من الإنترنت، تحليل مشاعرها وسيكولوجية السوق باستخدام تقنيات معالجة اللغة الطبيعية (NLP)، ومن ثم حفظ النتائج في قاعدة بيانات آمنة.

---

## 🚀 ميزات المشروع (Features)
* **Web Scraping:** سحب عناوين الأخبار المالية بشكل حي وتلقائي مع تخطي حمايات السيرفرات.
* **AI Sentiment Analysis:** تحليل قطبية المشاعر (Positive, Negative, Neutral) بدقة رقمية محصورة بين -1 و 1.
* **Secure Database:** حفظ البيانات بشكل دائم وآمن في قاعدة بيانات `SQLite` باستخدام *Parameterized Queries* لمنع اختراقات الـ SQL Injection.

---

## 🛠️ التقنيات المستخدمة (Tech Stack)
* **Python 3.x**
* **BeautifulSoup4** (لسحب البيانات)
* **TextBlob** (لذكاء تحليل المشاعر)
* **SQLite3** (لقاعدة البيانات)

---

## 📦 طريقة التشغيل (How to Run)

1. قم بتركيب المكتبات اللازمة:
```bash
pip install beautifulsoup4 textblob requests

python main.py
