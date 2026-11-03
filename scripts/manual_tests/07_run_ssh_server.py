# Run this in its own terminal/window and leave it running.
from honeypot import db, ssh_server

db.init_db()
ssh_server.serve(host="127.0.0.1", port=2222)
