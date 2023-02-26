
import threading
import sys

def record():
    print("recoding")

    
def stop():
    print("stopped recoding")

def run():
    while True:
        line = sys.stdin.readline().rstrip()
        
        if line == "record":
            record()
        elif line == "stop":
            stop()
