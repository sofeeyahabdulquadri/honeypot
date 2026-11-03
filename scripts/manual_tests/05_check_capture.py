import sqlite3
from honeypot import db

conn = sqlite3.connect(db.DB_PATH)
conn.row_factory = sqlite3.Row

print("--- connections ---")
for r in conn.execute("SELECT id, source_ip, started_at, closed_at FROM connections"):
    print(dict(r))

print("--- credentials ---")
for r in conn.execute("SELECT username, password, accepted FROM credentials"):
    print(dict(r))

print("--- commands ---")
for r in conn.execute("SELECT command, issued_at FROM commands"):
    print(dict(r))
