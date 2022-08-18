'''input
short
ports
'''

# Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2, 
# содержащих строчные буквы латинского алфавита.

import sys
from functools import lru_cache

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)
def edit_distance1(s1:str, s2:str) -> int: #превысит количество рекурсий
	@lru_cache(maxsize=None)
	def d(i:int, j:int) -> int:
		if i == 0 or j == 0: 
			return max(i, j)
		else: 
			return min(d(i, j-1)+1, d(i-1,j)+1, 
						d(i-1,j-1) + (s1[i-1] != s2[j-1]))
	return d(len(s1), len(s2))

def edit_distance2(s1:str, s2:str) -> int:
	m, n = len(s1), len(s2)
	if m < n: return edit_distance2(s2, s1)

	prev = list(range(n+1))
	for i, ch1 in enumerate(s1, 1):
		curr = [i]
		for j, ch2 in enumerate(s2, 1):
			curr.append(min(curr[-1]+1, prev[j]+1,
							prev[j-1] + (ch1 != ch2)))
		prev = curr	
	return prev[n]

def main():
	s1 = sys.stdin.readline()
	s2 = sys.stdin.readline()
	print(edit_distance2(s1, s2))

if __name__ == '__main__':
	main()
