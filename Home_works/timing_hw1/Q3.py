import time
import random
def find_max(list):
    max=list[0]
    length=len(list)
    for i in range(length):
        if list[i]>max:
            max=list[i]
    return max

list_10k = random.choices(range(-10**9, 10**9), k=10_000)
list_20k = random.choices(range(-10**9, 10**9), k=20_000)
list_40k = random.choices(range(-10**9, 10**9), k=40_000)
list_80k = random.choices(range(-10**9, 10**9), k=80_000)
list_160k = random.choices(range(-10**9, 10**9), k=160_000)
list_320k = random.choices(range(-10**9, 10**9), k=320_000)

start_time=time.perf_counter()
find_max(list_10k)
end_time=time.perf_counter()
print(end_time-start_time)

start_time=time.perf_counter()
find_max(list_20k)
end_time=time.perf_counter()
print(end_time-start_time)

start_time=time.perf_counter()
find_max(list_40k)
end_time=time.perf_counter()
print(end_time-start_time)

start_time=time.perf_counter()
find_max(list_80k)
end_time=time.perf_counter()
print(end_time-start_time)

start_time=time.perf_counter()
find_max(list_160k)
end_time=time.perf_counter()
print(end_time-start_time)

start_time=time.perf_counter()
find_max(list_320k)
end_time=time.perf_counter()
print(end_time-start_time)