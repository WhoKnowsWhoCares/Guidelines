'''input
5 1 5 8 12 13
5 8 1 23 1 11
'''

# В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных натуральных чисел, 
# не превышающих 10^9, в порядке возрастания, 
# во второй — целое число 1≤k≤10^5 и k натуральных чисел b1,…,bk, не превышающих 10^9. 
# Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi, или -1, если такого j нет.

import sys
from bisect import bisect_left # стандартный бинарный поиск 

def find_pos2(xs, query): # реализация через библиотеку
	low = bisect_left(xs, query)
	# i < low: xs[i] < query
	# i > low: xs[i] >= query
	if low < len(xs) and xs[low] == query: return low + 1
	else: return -1

def find_pos1(xs, query): # реализация своими силами
	# Invariant: low <= pos < high
	low, high = 0, len(xs)
	while low < high:
		mid = (low + high) // 2
		if query < xs[mid]: high = mid 		# [low, mid)
		elif query > xs[mid]: low = mid + 1 # [mid + 1, high)
		else: return mid + 1 
	return -1

def main():
	reader = (map(int, line.split()) for line in sys.stdin)
	n, *xs = next(reader)
	k, *queries = next(reader)
	assert n == len(xs)
	assert k == len(queries)
	for query in queries:
		print(find_pos2(xs, query), end=" ")

if __name__ == '__main__':
	main()