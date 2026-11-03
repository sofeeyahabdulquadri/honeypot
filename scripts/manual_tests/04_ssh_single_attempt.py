import time
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(
    "127.0.0.1", port=2222, username="root", password="toor123",
    timeout=10, look_for_keys=False, allow_agent=False,
)
print("authenticated")

chan = client.invoke_shell()
time.sleep(0.5)
print("banner:", repr(chan.recv(4096).decode(errors="replace")))

chan.send("whoami\n")
time.sleep(0.4)
print("whoami:", repr(chan.recv(4096).decode(errors="replace")))

chan.send("ls\n")
time.sleep(0.4)
print("ls:", repr(chan.recv(4096).decode(errors="replace")))

chan.send("exit\n")
time.sleep(0.4)
client.close()
print("session closed")
