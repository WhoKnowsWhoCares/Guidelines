'''input
5 9022
3316 1601
5375 8940
2852 6912
3336 9926
1717 8427
'''

'''input
3 50
60 20
100 50
120 30
'''

# Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6. 
# Каждая из следующих nn строк задаёт стоимость 0≤ci≤2⋅10^6 и объём 0<wi≤2⋅10^6 предмета 
# (n, W, ci, wi — целые числа). Выведите максимальную стоимость частей предметов 
# (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), 
# помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

import sys
import heapq

def fractional_knapsack1(capacity, val_and_weights):
	order = [(v/w, w) for v, w in val_and_weights]
	order.sort(reverse=True) #главное отсортировать
	acc = 0
	for v_per_w, w in order:
		if w < capacity:
			acc += v_per_w * w
			capacity -= w
		else:
			acc += v_per_w * capacity
			break 
	return acc

def fractional_knapsack2(capacity, val_and_weights):
	order = [(-v/w, w) for v, w in val_and_weights]
	heapq.heapify(order) # наверху кучи элемент с наименьшим приоритетом, поэтому "-v/w"
	acc = 0
	while order and capacity:
		v_per_w, w = heapq.heappop(order)
		can_take = min(w, capacity)
		acc -= v_per_w * can_take
		capacity -= can_take 
	return acc

def timed(func, *args, **kwargs):
	import time 

	start = time.perf_counter()
	value = func(*args, **kwargs)
	end = time.perf_counter()
	run_time = end - start
	# print(f"Time to run: {run_time:.2f}")
	return value

def test(func):
	assert func(0, [(60, 20)]) == 0.0
	assert func(25, [(60, 20)]) == 60.0
	assert func(25, [(60, 20), (0, 100)]) == 60.0
	assert func(25, [(60, 20), (50, 50)]) == 65.0

	from random import randint

	for attempt in range(100):
		n = randint(1, 1000)
		capacity = randint(0, 2* 10**6)
		val_and_weights = []
		for i in range(n):
			val_and_weights.append(
				(randint(0, 2* 10**6), randint(0, 2* 10**6)))
		t = timed(func, capacity, val_and_weights)
		assert t < 5 

	print("all done")


def main():
	reader = (tuple(map(int, line.split())) for line in sys.stdin)
	n, capacity = next(reader)
	val_and_weights = list(reader)
	assert len(val_and_weights) == n
	opt_value = fractional_knapsack2(capacity, val_and_weights)
	print(f"{opt_value:.3f}")

if __name__ == '__main__':
	# test(fractional_knapsack2)
	main()