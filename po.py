import process
import time
import subprocess

bp = process.PopenProcess(["python","lichess-bot.py"],"lichess-bot")

time.sleep(5)

while True:
    cmd = input(">").rstrip()
    try:
        bp.send_line(cmd)
    except:
        pass
    print("cmd sent")
    if cmd == "x":
        break

print("exiting...")
time.sleep(5)
print("done")