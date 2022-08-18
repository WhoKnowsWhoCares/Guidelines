'''input
4
4 7
1 3
2 5
5 6
'''

# По данным nn отрезкам необходимо найти множество точек минимального размера, 
# для которого каждый из отрезков содержит хотя бы одну из точек.

# В первой строке дано число 1≤n≤100 отрезков. 
# Каждая из последующих nn строк содержит по два числа 0^90≤l≤r≤10^9, задающих начало и конец отрезка.
# Выведите оптимальное число mm точек и сами mm точек. 
# Если таких множеств точек несколько, выведите любое из них.


import sys
import heapq

def greedy1(start_and_end) -> list:
	result = []
	hp = [[end, start] for start, end in start_and_end]
	heapq.heapify(hp)
	while hp:
		opt_point = heapq.heappop(hp)
		while True and hp:
			check = heapq.heappop(hp)
			if check[1] > opt_point[0]:
				heapq.heappush(hp, check)
				break
		result.append(opt_point[0])

	return result

def main():
	reader = (tuple(map(int, line.strip().split())) for line in sys.stdin)
	n = next(reader)
	start_and_end = list(reader)
	# assert len(start_and_end) == n
	opt_points = greedy1(start_and_end)
	print(len(opt_points))
	print(" ".join(map(str,opt_points)))
	

if __name__ == "__main__":
	main()