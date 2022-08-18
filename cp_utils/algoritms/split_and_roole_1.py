'''input
5
2 3 9 2 9
'''

import sys
from collections import Counter 

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

c = Counter(arr)
s = sorted(list(set(arr)))

for i in s:
	print(f"{i} "*c[i], end="")
