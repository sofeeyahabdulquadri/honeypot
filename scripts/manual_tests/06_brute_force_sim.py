import time
import paramiko

attempts = [
    ("root", "toor"), ("root", "123456"), ("admin", "admin"),
    ("ubuntu", "ubuntu"), ("root", "qwerty123"), ("test", "test123"),
]

for user, pw in attempts:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            "127.0.0.1", port=2222, username=user, password=pw,
            timeout=5, look_for_keys=False, allow_agent=False,
        )
        chan = client.invoke_shell()
        time.sleep(0.2)
        chan.recv(4096)
        chan.send("id\n")
        time.sleep(0.2)
        chan.recv(4096)
        chan.send("exit\n")
        time.sleep(0.2)
        client.close()
        print(f"{user}:{pw} -> logged in and ran id")
    except Exception as e:
        print(f"{user}:{pw} -> failed: {e}")
