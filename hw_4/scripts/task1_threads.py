import threading
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def single_thread_run(n):
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    print(f"Single thread result: {result}, Time taken: {end_time - start_time} seconds")


def multi_thread_run(n, thread_count):
    threads = []
    start_time = time.time()
    for _ in range(thread_count):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Multi-thread run with {thread_count} threads, Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    n = 35

    print("Running with a single thread...")
    single_thread_run(n)

    thread_count = 10
    print(f"Running with {thread_count} threads...")
    multi_thread_run(n, thread_count)
