# НЕ ДОДЕЛАНА

'''input
7419 7
2 3 4 8 10 400 7000
'''

# Первая строка входа содержит целые числа 1≤W≤10^4 и 1≤n≤300 — вместимость рюкзака и число золотых слитков. 
# Следующая строка содержит nn целых чисел 0≤w1,…,wn≤10^5, задающих веса слитков. 
# Найдите максимальный вес золота, который можно унести в рюкзаке.

import sys
from functools import lru_cache

sys.setrecursionlimit(10000)
def knapsack1(arr:list, w:int) -> int:
	@lru_cache(maxsize=None)
	def d(w:int) -> int:
		v = 0
		for i in range(len(arr)):
			if arr[i] <= w:
				v = max(v, d(w-arr[i])+1)
		return v
	return d(w)

def restore(arr:list, max_len:list):
	curr_len = max(max_len)
	prev_val = 0
	for i in range(len(arr)-1,-1,-1):
		if max_len[i]==curr_len and curr_len-arr[i] == 0:
			print(arr[i], end=" ")
			curr_len -= 1
			prev_val = arr[i]

def main():
	n, m = map(int,sys.stdin.readline().strip().split())
	arr = list(map(int,sys.stdin.readline().strip().split()))
	max_w = knapsack1(arr, n)
	print(max_w)

if __name__ == '__main__':
	main()