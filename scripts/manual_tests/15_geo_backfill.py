import sqlite3
from honeypot import db

conn = sqlite3.connect(db.DB_PATH)
conn.execute(
    "INSERT INTO connections (source_ip, source_port, protocol, started_at) "
    "VALUES ('1.1.1.1', 1234, 'ssh', datetime('now'))"
)
conn.commit()
print("inserted a connection with no geo data yet")
