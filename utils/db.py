import sqlite3
import os

os.makedirs("data", exist_ok=True)
DB_PATH = "data/history.db"

# Will now create a fresh schema with pdf_path
with sqlite3.connect(DB_PATH) as conn:
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        preset TEXT,
        score INTEGER,
        result TEXT,
        pdf_path TEXT
    )''')
    conn.commit()

def store_report(name, email, preset, score, result, pdf_path):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''
            INSERT INTO reports (name, email, preset, score, result, pdf_path)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, email, preset, score, result, pdf_path))
        conn.commit()

def get_all_reports():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT id, name, email, preset, score, result, pdf_path FROM reports")
        return c.fetchall()
