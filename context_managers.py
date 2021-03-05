from contextlib import contextmanager
import time

# function based
@contextmanager
def time_this():
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('elapsed: {}'.format(end - start))


def sample_function():
    for i in range(100):
        i==i+1


with time_this():
    sample_function()
