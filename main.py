import time
import sys

def animated_progress_bar(max_value):
    for i in range(max_value + 1):
        sys.stdout.write(f"\rProgress: [{i * '#'}{max_value * '-'}] {i * 100 / max_value}%")
        sys.stdout.flush()
        time.sleep(0.1)

animated_progress_bar(100)
