'''input
abcdabcbdab
'''

'''
Для заданной строки строки s=s_0 s_1...s_(n-1) её 
z-функцией является массив z длины n, проиндексированный от 0 до n-1, 
что z[i] — это длина наидлиннейшего общего префикса всей строки s и её суффикса s[i … n-1].
Для i=0 обычно z[0] = 0 (иногда удобно считать, что z[0] = n).
'''

import sys 

def z_function(s:str) -> list:
	l = r = 0
	z = [0]*len(s)
	for i in range(1,len(s)):
		if r >= i:
			z[i] = min(z[i-l],r-i+1)
		while z[i]+i < len(s) and s[z[i]] == s[z[i]+i]:
			z[i] += 1
		if i+z[i]-1 > r:
			l = i
			r = i+z[i]-1
	return z

def main():
	s = sys.stdin.readline()
	z = z_function(s)
	print(z)


if __name__ == '__main__':
	main()