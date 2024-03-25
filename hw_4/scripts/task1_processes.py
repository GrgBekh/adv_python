from multiprocessing import Pool
import time


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def single_process_run(n):
    start_time = time.time()
    result = fibonacci(n)
    end_time = time.time()
    print(f"Single process result: {result}, Time taken: {end_time - start_time} seconds")


def multi_process_run(n, process_count):
    start_time = time.time()
    with Pool(process_count) as pool:
        result = pool.apply(fibonacci, (n,))
    end_time = time.time()
    print(f"Multi-process result: {result}, Time taken: {end_time - start_time} seconds")


if __name__ == "__main__":
    n = 35  # Fixed Fibonacci number to calculate

    print("Running with a single process...")
    single_process_run(n)

    process_count = 10  # Number of processes
    print(f"Running with {process_count} processes...")
    multi_process_run(n, process_count)
