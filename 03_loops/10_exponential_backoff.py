import time

wait_time = 1
max_retires = 5
retries = 0

while retries < max_retires:
    print("Attempt",retries + 1, f"wait time {wait_time} secs" )
    time.sleep(wait_time)
    retries += 1
    wait_time *= 2