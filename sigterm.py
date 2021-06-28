import signal
import time
run = True

def handler_stop_signals(signum, frame):
    global run
    print(signum)
    run = False

signal.signal(signal.SIGABRT, handler_stop_signals)
signal.signal(signal.SIGBREAK, handler_stop_signals)
signal.signal(signal.SIGFPE, handler_stop_signals)
signal.signal(signal.SIGILL, handler_stop_signals)
signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGSEGV, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)

SIG_DFL = 0
SIG_IGN = 1

cnt = 0

while run:
    ++cnt
    print(cnt)
    time.sleep(1)

print("DONE")
