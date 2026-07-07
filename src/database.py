import sqlite3

def init_db():
    conn = sqlite3.connect("market_data.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news_sentiment  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    headline TEXT NOT NULL,
    sentiment Text NOT NULL,
    score REAL NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def save_news_sentiment(headline, sentiment, score):
        conn = sqlite3.connect("market_data.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO news_sentiment (headline, sentiment, score)
            VALUES (?, ?, ?)
            """, (headline, sentiment, score))

        conn.commit()
        conn.close()

