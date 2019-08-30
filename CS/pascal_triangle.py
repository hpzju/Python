"""
description: Pascal Triangle singleton class
class: PascalTriangle()
method:
    PascalTriangle(n: int) returns n-level triangle and print it
    format(n: int) returns n-level stringified triangle and print it
"""


import time
import sys
import tracemalloc
import gc


class PascalTriangle(object):

    __triangle = []
    __instance = None
    _gen = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, n=0):
        PascalTriangle._gen = gen_binomial()
        PascalTriangle._get_triangle(n)

    @classmethod
    def __call__(cls, n):
        # cls.format(n)
        return cls._get_triangle(n)

    def __repr__(self):
        return f"PascalTriangle()"

    @classmethod
    def _get_triangle(cls, n):
        start = len(cls.__triangle)
        if start <= n:
            print(f"generate new row: {start} -> {n}")
            for i in range(start, n+1):
                cls.__triangle.append(next(cls._gen))
        return cls.__triangle[:n+1]

    @classmethod
    def format(cls, n=-1):
        if n < 0:
            pascal = cls.__triangle
        else:
            pascal = cls._get_triangle(n)

        block_len = len(str(max(pascal[-1])))+1
        block_num = len(pascal[-1])

        fmttriangle = []

        for row in range(len(pascal)):
            pad_len = (block_num-row-1)*block_len//2
            padding = " "*pad_len
            fmt = f"{{:^{block_len}}}"*(row+1)
            fmtrow = padding + fmt.format(*pascal[row]) + padding
            fmttriangle.append(fmtrow)
            print(fmtrow)

        return fmttriangle


def gen_binomial():
    g_logs = 100
    coefficients = (1,)
    yield coefficients
    coefficients = (1, 1)
    yield coefficients
    while True:
        coefficients = tuple(next_binomial(coefficients))
        if len(coefficients) == g_logs:
            status = tracemalloc.take_snapshot().statistics("lineno")
            print(f"{g_logs}: {status[0].size/1024/1024} MB")
            gc.collect()
            g_logs += 300
        yield coefficients


g_log = 100


def next_binomial(coefficients):
    global g_log
    if len(coefficients) == 0:
        return 1,
    elif len(coefficients) == 1:
        return 1,1
    else:
        new_coefficients = [1 if index == 0 else coefficients[index-1]+coefficients[index]
                            for index in range(len(coefficients))]
        new_coefficients.append(1)

        # if len(coefficients) == g_log:
        #     status = tracemalloc.take_snapshot().statistics("lineno")
        #     print(f"b({g_log}): {status[0].size / 1024 / 1024} MB")
        #     print(f"sizeof(coefficients) = {sys.getsizeof(new_coefficients)/ 1024 / 1024} MB")
        #     g_log += 300

        return tuple(new_coefficients)


g_logs = 100


def gen_next_binomial(coefficients):
    global g_logs
    yield 1
    for index in range(len(coefficients)-1):
        yield coefficients[index]+coefficients[index+1]
    yield 1
    if len(coefficients) == g_logs:
        status = tracemalloc.take_snapshot().statistics("lineno")
        print(f"{g_logs}: {status[0].size / 1024 / 1024} MB")
        g_logs += 300
    raise StopIteration


if __name__ == '__main__':
    pt = PascalTriangle(10)
    pt.format(5)
    pt(50)

    # start = time.time()
    # tracemalloc.stop()
    # tracemalloc.clear_traces()
    # tracemalloc.start()
    # arr = pt(1000)
    # end = time.time()
    # print(f"elapsed: {end-start}")
    # print(f"size(arr): {sys.getsizeof(arr) / 1024 / 1024}MB")
    # print(f"size(gen): {sys.getsizeof(PascalTriangle._gen) / 1024 / 1024}MB")
    # print(f"size(PascalTriangle): {sys.getsizeof(PascalTriangle)/1024/1024}MB")

    # start = time.time()
    # arr = pt(5000)
    # end = time.time()
    # print(f"elapsed: {end-start}")
    # print(f"size: {sys.getsizeof(arr) / 1024 / 1024}MB")
    # print(f"size: {sys.getsizeof(PascalTriangle._gen) / 1024 / 1024}MB")
    # print(f"size: {sys.getsizeof(PascalTriangle)/1024/1024}MB")

    start = time.time()
    tracemalloc.stop()
    tracemalloc.clear_traces()
    tracemalloc.start()
    a = []
    for i in range(4000):
        a = next_binomial(a)
        # print(f"size: {sys.getsizeof(a) / 1024 / 1024:6.2}MB")
    end = time.time()
    print(f"size({a[1]}): {sys.getsizeof(a) / 1024 / 1024:6.2}MB")
    print(f"elapsed: {end-start}")

    # start = time.time()
    # tracemalloc.stop()
    # tracemalloc.clear_traces()
    # tracemalloc.start()
    # a =
    # for i in range(3000):
    #     pre = [] if len(a) == 0 else a[-1]
    #     a.append(next_binomial(pre))
    #     # print(f"size: {sys.getsizeof(a) / 1024 / 1024:6.2}MB")
    # end = time.time()
    # print(a[-1][1])
    # print(f"elapsed: {end-start}")

    # start = time.time()
    # tracemalloc.stop()
    # tracemalloc.clear_traces()
    # tracemalloc.start()
    # gen = gen_binomial()
    # a = []
    # for i in range(5000):
    #     a.append(next(gen))
    #     # print(f"size: {sys.getsizeof(a) / 1024 / 1024:6.2}MB")
    # end = time.time()
    # print(f"elapsed: {end-start}")