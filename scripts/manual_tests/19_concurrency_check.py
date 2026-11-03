import sqlite3
from honeypot import db

conn = sqlite3.connect(db.DB_PATH)
print("connections:", conn.execute("SELECT COUNT(*) FROM connections").fetchone()[0])
print("credentials:", conn.execute("SELECT COUNT(*) FROM credentials").fetchone()[0])
