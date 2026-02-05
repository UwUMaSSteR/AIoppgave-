import sqlite3
from datetime import datetime

DB_NAME = "vlc_updates.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS updates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            version TEXT,
            checked_at TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_version(version):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("INSERT INTO updates (version, checked_at) VALUES (?, ?)",
              (version, datetime.now().isoformat()))

    conn.commit()
    conn.close()

def get_last_version():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT version FROM updates ORDER BY id DESC LIMIT 1")
    result = c.fetchone()

    conn.close()

    return result[0] if result else None
