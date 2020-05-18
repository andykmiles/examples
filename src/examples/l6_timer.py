import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Ran {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer



@timer
def long_f():
    for num in range(0,4):
        time.sleep(.5)


@timer
def shorter_f():
    for num in range(0,9):
        time.sleep(.2)

print(long_f())
print(shorter_f())
