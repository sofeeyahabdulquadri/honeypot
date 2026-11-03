from honeypot import ssh_server

key = ssh_server.ensure_host_key()
print(key.get_name(), key.get_fingerprint().hex())
