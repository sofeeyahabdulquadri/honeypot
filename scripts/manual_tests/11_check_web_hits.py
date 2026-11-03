import sqlite3
from honeypot import db

conn = sqlite3.connect(db.DB_PATH)
conn.row_factory = sqlite3.Row
for r in conn.execute(
    "SELECT source_ip, path, method, username, password "
    "FROM web_hits ORDER BY id DESC LIMIT 6"
):
    print(dict(r))
