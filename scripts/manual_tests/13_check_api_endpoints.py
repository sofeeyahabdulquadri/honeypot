import json
import urllib.request

endpoints = [
    "/api/summary",
    "/api/timeseries?hours=24",
    "/api/geo-distribution",
    "/api/credentials/top?limit=10",
    "/api/connections?limit=10",
    "/api/commands?limit=10",
]

base = "http://127.0.0.1:8080"
for ep in endpoints:
    with urllib.request.urlopen(base + ep) as resp:
        data = json.loads(resp.read())
        print(f"{ep} -> {resp.status}, {len(data) if isinstance(data, list) else 'dict'} items")
