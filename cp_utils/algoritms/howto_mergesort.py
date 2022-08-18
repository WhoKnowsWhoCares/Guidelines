'''input
5
2 3 9 2 9
'''
# Сортировка слиянием

import sys
import time

def merge(lst1, lst2):
	global reverse_count
	i1, i2 = 0, 0
	res = []
	while i1 < len(lst1) or i2 < len(lst2):
		if i2 == len(lst2) or (i1 < len(lst1) and lst1[i1] <= lst2[i2]):
			res.append(lst1[i1])
			i1 += 1
		else:
			# lst1[i1, i1+1, ... len(lst1)-1] > lst2[i2]
			reverse_count += (len(lst1) - i1)
			res.append(lst2[i2])
			i2 += 1
	return res

def mergeSort1(lst:list) -> list:
	if len(lst) > 1:
		mid = len(lst)//2
		left = lst[:mid] 
		right = lst[mid:]
		left = mergeSort1(left)
		right = mergeSort1(right)
		lst = merge(left, right)
	return lst


def mergeSort2(lst):
	queue = []
	for i in range(len(lst)):
		queue.append([lst[i]])
	while len(queue) > 1:
		lst1 = queue.pop()
		lst2 = queue.pop()
		res_lst = merge(lst1, lst2)
		queue.append(res_lst)
	return queue.pop()

def main():
	global reverse_count
	reverse_count = 0
	start = time.perf_counter()
	n = int(sys.stdin.readline())
	lst = list(map(int, sys.stdin.readline().strip().split()))
	lst = mergeSort1(lst)
	end = time.perf_counter()
	run_time = end - start
	print(*lst)
	print(f"Inversion count: {reverse_count}")

if __name__ == '__main__':
	main()