import math
import concurrent
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import logging


def integrate_section(f, a, b, n_iter):
    logging.info(f"Starting task for integration from {a} to {b} with {n_iter} iterations")
    return integrate(f, a, b, n_iter=n_iter)


def parallel_integration_threads(f, a, b, *, n_jobs, n_iter):
    results = []
    splits = [n_iter // n_jobs] * n_jobs
    remainder = n_iter % n_jobs
    for i in range(remainder):
        splits[i] += 1

    def integrate_section_inner(a, b, n_iter):
        logging.info(f"Starting task for integration from {a} to {b} with {n_iter} iterations")
        return integrate(f, a, b, n_iter=n_iter)

    with ThreadPoolExecutor(max_workers=n_jobs) as executor:
        futures = []
        for i in range(n_jobs):
            left_bound = a + (b - a) / n_jobs * i
            right_bound = a + (b - a) / n_jobs * (i + 1)
            n_iter_split = splits[i]
            futures.append(executor.submit(integrate_section_inner, left_bound, right_bound, n_iter_split))

        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    total_result = sum(results)
    return total_result


def parallel_integration_processes(f, a, b, *, n_jobs, n_iter):
    results = []
    splits = [n_iter // n_jobs] * n_jobs
    remainder = n_iter % n_jobs
    for i in range(remainder):
        splits[i] += 1

    with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
        futures = []
        for i in range(n_jobs):
            left_bound = a + (b - a) / n_jobs * i
            right_bound = a + (b - a) / n_jobs * (i + 1)
            n_iter_split = splits[i]
            futures.append(executor.submit(integrate_section, f, left_bound, right_bound, n_iter_split))

        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    total_result = sum(results)
    return total_result


def integrate(f, a, b, *, n_iter=100000):
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


if __name__ == "__main__":

    log_filename = '../artifacts/integration_logs.log'
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - Process %(process)d - Task: %(message)s',
                        filename=log_filename, filemode='w')
    print('\n')
    print("Integrating with threads\n")
    for job_num in range(1, 33):
        start_time = time.time()
        val = parallel_integration_threads(math.cos, 0, math.pi / 2, n_jobs=job_num, n_iter=30000000)
        end_time = time.time()
        print(f"Result: {val}, Time taken: {end_time - start_time} seconds with {job_num} threads")

    print('\n')
    print("Integrating with processes\n")

    for job_num in range(1, 33):
        start_time = time.time()
        val = parallel_integration_processes(math.cos, 0, math.pi / 2, n_jobs=job_num, n_iter=30000000)
        end_time = time.time()
        print(f"Result: {val}, Time taken: {end_time - start_time} seconds with {job_num} processes")
