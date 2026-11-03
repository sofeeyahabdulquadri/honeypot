import urllib.request
import urllib.parse

attempts = [
    ("admin", "admin"), ("root", "root"),
    ("admin", "P@ssw0rd"), ("test", "test"),
]

for user, pw in attempts:
    data = urllib.parse.urlencode({"username": user, "password": pw}).encode()
    req = urllib.request.Request("http://127.0.0.1:8080/login", data=data, method="POST")
    with urllib.request.urlopen(req) as resp:
        print(f"{user}:{pw} -> {resp.status}")
