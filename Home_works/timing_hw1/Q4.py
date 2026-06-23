import random
import time

def count_duplicate_pairs(lst):
    count = 0

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                count += 1

    return count


sizes = [500, 1000, 2000, 4000, 8000]

for n in sizes:
    lst = [random.randint(1, 100) for _ in range(n)]

    start_time = time.perf_counter()
    pairs = count_duplicate_pairs(lst)
    end_time = time.perf_counter()

    print(
        f"n={n:5d} | time={end_time-start_time} sec"
    )