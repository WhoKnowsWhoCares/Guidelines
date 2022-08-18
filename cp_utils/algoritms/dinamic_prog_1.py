'''input
10
2 6 7 7 12 21 36 42 84 168
'''

# Дано целое число 1≤n≤10^3 и массив A[1…n] натуральных чисел, не превосходящих 2*10^9. 
# Выведите максимальное 1≤k≤n, для которого найдётся подпоследовательность 1≤i1<i2<…<ik≤n длины k, 
# в которой каждый элемент делится на предыдущий (формально: для  всех 1≤j<k, A[ij]∣A[ij+1]).

import sys

def dinamic(arr:list) -> int:
	max_len = [1] #массив с макс подпоследовательностью, заканч в соотв эл-те массива arr
	for i in range(1,len(arr)):
		curr = 1
		for j in range(i-1,-1,-1):
			if arr[i] % arr[j] == 0:
				curr = max(curr, max_len[j] + 1)
			# print(f"{arr[i]}:{arr[j]}:{max_len[j]}:{arr[i] % arr[j]}")
		max_len.append(curr)
		# print(curr)
	# print(*max_len)
	return max_len

def restore(arr:list, max_len:list):
	curr_len = max(max_len)
	prev_val = 0
	for i in range(len(arr)-1,-1,-1):
		if max_len[i]==curr_len and prev_val % arr[i] == 0:
			print(arr[i], end=" ")
			curr_len -= 1
			prev_val = arr[i]

def main():
	n = int(sys.stdin.readline())
	arr = list(map(int,sys.stdin.readline().strip().split()))
	max_len = dinamic(arr)
	print(max(max_len))
	restore(arr, max_len)

if __name__ == '__main__':
	main()