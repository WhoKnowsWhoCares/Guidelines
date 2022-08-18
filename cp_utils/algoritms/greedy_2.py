'''input
2
'''

# По данному числу 1≤n≤10^9 найдите максимальное число k, 
# для которого n можно представить как сумму k различных натуральных слагаемых. 
# Выведите в первой строке число k, во второй — k слагаемых.

import sys 

def greedy2(n):
	sum_num = 0
	counter = 1
	additives = []
	while True:
		if sum_num + counter > n: break
		sum_num += counter
		additives.append(counter)
		counter += 1
	additive = n - sum_num
	if  additive <= counter-1: 
		additives[len(additives)-1] += (n-sum_num)
	return additives

def main():
	n = int(sys.stdin.readline())
	sum_num = greedy2(n)
	print(len(sum_num))
	print(*sum_num)

if __name__ == "__main__":
	main()