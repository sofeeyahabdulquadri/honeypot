import urllib.request
import urllib.parse

data = urllib.parse.urlencode({"username": "admin", "password": "letmein123"}).encode()
req = urllib.request.Request("http://127.0.0.1:8080/login", data=data, method="POST")
with urllib.request.urlopen(req) as resp:
    print("status:", resp.status)
