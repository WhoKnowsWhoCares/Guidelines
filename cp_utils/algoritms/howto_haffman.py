'''input
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
'''

# Для проверки huffman_encode
# '''input
# asdfasdf
# '''

from collections import Counter, namedtuple
import heapq
import sys

class Node(namedtuple("Node", ["left", "right"])):
	def walk(self, code, acc):
		self.left.walk(code, acc + "0")
		self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
	def walk(self, code, acc):
		code[self.char] = acc or "0"


def huffman_encode(s): 
	h = []
	for ch, freq in Counter(s).items():
		h.append((freq, len(h), Leaf(ch)))

	heapq.heapify(h)
	count = len(h)
	while len(h) > 1:
		freq1, _count1, left = heapq.heappop(h)
		freq2, _count2, right = heapq.heappop(h)
		heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
		count += 1
	
	code = {}
	if h:
		[(_freq, _count, root)] = h
		root.walk(code,"")

	return code

def huffman_decode(encoded, codes):
	buffer = ''
	decode = {}
	result = ''
	for ch, code in codes.items():
		decode[code] = ch
	for i in encoded:
		buffer = buffer + i
		ch = decode.get(buffer)
		if ch:
			buffer = ''
			result = result + ch
	return result


def test(n_iter=100):
	import random
	import string
	for i in range(n_iter):
		length = random.randint(0, 32)
		s = "".join(random.choice(string.ascii_letters) for _ in range(length))
		code = huffman_encode(s)
		encoded = "".join(code[ch] for ch in s)
		assert huffman_decode(encoded, code) == s
	print('Well done!')

def main_encode(): #Для huffman_encode
	s = input()
	code = huffman_encode(s)
	encoded = "".join(code[ch] for ch in s)
	print(len(code), len(encoded))
	for ch in sorted(code):
		print(f"{ch}: {code[ch]}")
	print(encoded)

def main_decode(): #Для huffman_decode
	n, enc_length = sys.stdin.readline().strip().split()
	codes = {}
	for _ in range(int(n)):
		ch, code = sys.stdin.readline().strip().split(': ')
		codes[ch] = code
	encoded = sys.stdin.readline().strip()
	# assert len(encoded) == enc_length
	decoded = huffman_decode(encoded, codes)
	print(decoded)

if __name__ == "__main__":
	# main_encode()
	# main_decode()
	test()