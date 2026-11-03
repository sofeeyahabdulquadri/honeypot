from honeypot.web import create_app

app = create_app()
client = app.test_client()

assert client.get("/").status_code == 200
assert client.get("/dashboard").status_code == 200

r = client.post("/login", data={"username": "admin", "password": "hunter2"})
assert r.status_code == 200

r = client.get("/api/summary")
assert r.status_code == 200
print(r.get_json())
print("OK: routes respond")
