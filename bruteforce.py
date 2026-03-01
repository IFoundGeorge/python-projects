import string
import itertools
import multiprocessing as mp
import time
import os

characters = string.ascii_letters + string.digits

def worker(args):
    start_char, target, max_length = args
    count = 0
    start_time = time.time()

    for length in range(1, max_length + 1):

        if length == 1:
            attempt = start_char
            count += 1
            if attempt == target:
                return attempt
            continue

        for combo in itertools.product(characters, repeat=length - 1):
            attempt = start_char + ''.join(combo)
            count += 1

            if count % 500000 == 0:
                elapsed = time.time() - start_time
                speed = count / elapsed
                print(f"[PID {os.getpid()}] {int(speed)} guesses/sec")

            if attempt == target:
                return attempt

    return None


if __name__ == "__main__":
    target_password = input("Enter password (max 12 chars): ")
    max_length = 12

    start_time = time.time()
    cpu_count = mp.cpu_count()

    print(f"Using {cpu_count} CPU cores...\n")

    with mp.Pool(cpu_count) as pool:
        tasks = [(char, target_password, max_length) for char in characters]

        for result in pool.imap_unordered(worker, tasks):
            if result:
                print("\nPassword cracked!")
                print("Password:", result)
                print("Time:", round(time.time() - start_time, 2), "seconds")
                pool.terminate()
                break