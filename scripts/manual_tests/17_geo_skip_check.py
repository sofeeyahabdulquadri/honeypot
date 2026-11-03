from honeypot.geoip import _is_skippable

assert _is_skippable("127.0.0.1") is True
assert _is_skippable("10.0.0.5") is True
assert _is_skippable("192.168.1.1") is True
assert _is_skippable("172.16.0.1") is True
assert _is_skippable("172.32.0.1") is False  # outside the 172.16-31 private range
assert _is_skippable("8.8.8.8") is False
print("OK: private-range filtering works as expected")
