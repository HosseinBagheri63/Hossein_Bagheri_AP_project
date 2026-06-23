import time
def how_many_times_half_recursive(n):
    count=0
    if n<=1:
        return count
    else:
        n=n//2
        return how_many_times_half(n)+1
def how_many_times_half(n):
    count=0
    while n>1:
        n=n//2
        count+=1
    return count
n=2**10
for i in range(5):
    start_time=time.perf_counter()
    how_many_times_half(n)
    end_time=time.perf_counter()
    print(end_time-start_time)
    n= n**10

