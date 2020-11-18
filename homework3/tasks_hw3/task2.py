"""
Here's a not very efficient calculation function that calculates something important::

    import time
    import struct
    import random
    import hashlib

    def slow_calculate(value):
        ""Some weird voodoo magic calculations""
        time.sleep(random.randint(1,3))
        data = hashlib.md5(str(value).encode()).digest()
        return sum(struct.unpack('<' + 'B' * len(data), data))

Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""

import hashlib
import multiprocessing
import os
import random
import struct
import time


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def runtime_timer(f):
    def wrapper(func, value):
        start_time = time.time()
        result = f(func, value)
        stop_time = time.time()
        run_time = f"{stop_time-start_time:.2f}"
        return result, run_time

    return wrapper


def mproc_sum(func, *args):
    with multiprocessing.Pool(os.cpu_count() * 7) as p:
        return sum(p.map(func, range(*args)))
