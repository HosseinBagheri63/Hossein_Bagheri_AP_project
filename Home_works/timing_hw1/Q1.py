import time
import random

def first_item(list):
    if list:
        return list[0]
    else:
        return None

list_100 = random.choices(range(-10**9, 10**9), k=100)
list_10k = random.choices(range(-10**9, 10**9), k=10_000)
list_1m = random.choices(range(-10**9, 10**9), k=1_000_000)
list_100m = random.choices(range(-10**9, 10**9), k=100_000_000)

start_time=time.perf_counter()
first_item(list_100)
end_time = time.perf_counter()
print(end_time - start_time)

start_time = time.perf_counter()
first_item(list_10k)
end_time = time.perf_counter()
print(end_time - start_time)

start_time=time.perf_counter()
first_item(list_1m)
end_time = time.perf_counter()
print(end_time - start_time)

start_time=time.perf_counter()
first_item(list_100m)
end_time = time.perf_counter()
print(end_time - start_time)