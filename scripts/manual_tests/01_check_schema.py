from honeypot import db

db.init_db()

import sqlite3
conn = sqlite3.connect(db.DB_PATH)
tables = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")]
print(tables)
assert {"connections", "credentials", "commands", "web_hits", "geo_cache"} <= set(tables)
print("OK: all tables present")
