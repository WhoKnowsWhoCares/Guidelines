'''input
3
'''

import sys
import functools
import timeit
import time

def timed(func, *args, **kwargs):
	start = time.perf_counter()
	value = func(*args, **kwargs)
	end = time.perf_counter()
	run_time = end - start
	print(f"Time to run: {run_time:.2f}")
	return value
	
def fib1(m): #долго из-за постоянного пересчета
	assert m >= 0
	return m if m <= 1 else fib1(m-1)+fib1(m-2)

cache = {}
def fib2(m): #глобальный кэш - плохо
	assert m >= 0
	if m not in cache:
		cache[m] = m if m <= 1 else fib2(m-1)+fib2(m-2)
	return cache[m]

def memo(f): #декоратор кэша для fib1
	cache = {}
	def inner(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return inner

fib3 = memo(fib1)

from functools import lru_cache #декоратор кэша стандартными средствами
fib4 = lru_cache(maxsize=None)(fib1)

def fib5(m):
	assert m >= 0
	f0, f1 = 0, 1
	for _ in range(m-1):
		f0, f1 = f1, f0+f1
	return f1

# def main():
# 	m = map(int,sys.stdin.readline().strip().split())
# 	res = fib1(m)
# 	print(res)


# if __name__ == '__main__':
#     main()

print(timed(fib1,16))
# print(timeit.timeit('fib1(16)', globals=globals()))
# print(timed(fib2,31))
# print(timed(fib3,31))
# print(timed(fib4,31))
# print(timed(fib5,31))