import threading
import time
import paramiko


def attempt(n):
    try:
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(
            "127.0.0.1", port=2222, username=f"user{n}", password=f"pass{n}",
            timeout=10, look_for_keys=False, allow_agent=False,
        )
        chan = c.invoke_shell()
        time.sleep(0.3)
        chan.recv(4096)
        chan.send("whoami\n")
        time.sleep(0.3)
        chan.recv(4096)
        chan.send("exit\n")
        time.sleep(0.2)
        c.close()
    except Exception as e:
        print(f"thread {n} failed: {e}")


threads = [threading.Thread(target=attempt, args=(i,)) for i in range(20)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print("all 20 concurrent connections finished")
