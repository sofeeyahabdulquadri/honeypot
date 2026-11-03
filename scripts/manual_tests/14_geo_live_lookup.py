import time
from honeypot.geoip import enricher
from honeypot import db

enricher.start()
enricher.submit("8.8.8.8")
time.sleep(3)

row = db.get_cached_geo("8.8.8.8")
print(dict(row) if row else "not resolved yet -- try increasing the sleep")
