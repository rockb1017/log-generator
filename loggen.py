import os
from time import sleep
from datetime import datetime

MESSAGE_COUNT = int(os.getenv("MESSAGE_COUNT", 10000))
SIZE = int(os.getenv("SIZE", 128))
FREQ = float(os.getenv("FREQ", "1"))

MESSAGE_COUNT = max(MESSAGE_COUNT, 5)
MY_HOST = os.getenv("MY_HOST", os.uname()[1])


def print_beginning():
    print("---begin---")


def print_ending():
    later = datetime.now()
    print("generated %d messages in %d seconds" % (MESSAGE_COUNT, int((later - now).total_seconds())))
    print("EPS: %d" % (MESSAGE_COUNT / (later - now).total_seconds()))
    print("---end---")


def print_log(i):
    log_meta = " ".join(["num:", str(i), "|", MY_HOST, "|", datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"), "|"])
    print(log_meta, "r"*(max(1, SIZE-len(log_meta))))
    sleep(FREQ)
    

now = datetime.now()

i = 1
if MESSAGE_COUNT <= 0:
    print_beginning()
    while True:
        print_log(i)
        i += 1
else:
    print_beginning()
    while i <= MESSAGE_COUNT - 4:
        print_log(i)
        i += 1
    print_ending()

while True:
    sleep(60)

