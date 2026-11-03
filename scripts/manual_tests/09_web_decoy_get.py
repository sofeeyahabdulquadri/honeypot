import urllib.request

with urllib.request.urlopen("http://127.0.0.1:8080/") as resp:
    body = resp.read().decode()
    print("status:", resp.status)
    assert "Sign in" in body
    print("OK: decoy login page served")
