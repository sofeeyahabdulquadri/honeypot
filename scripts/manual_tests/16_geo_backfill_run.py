import time
from honeypot.geoip import enricher
from honeypot import db

enricher.start()
enricher.backfill_missing()
time.sleep(3)

row = db.get_cached_geo("1.1.1.1")
print(dict(row) if row else "not resolved")
