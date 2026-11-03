# Run this in its own terminal/window and leave it running.
from honeypot.web import create_app

app = create_app()
app.run(host="127.0.0.1", port=8080)
