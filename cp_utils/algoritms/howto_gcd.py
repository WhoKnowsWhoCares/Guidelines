# GCD = НОД (наибольший общий делитель)

def gcd1(a, b):
	assert a>=0 and b>=0
	for d in reversed(range(0,max(a,b)+1)):
		if d == 0 or a%d == b%d == 0: return d

def gcd2(a, b):
	assert a >= 0 and b >=0
	while a and b:
		if a >= b: a %= b 
		else: b %= a 
	return max(a,b)

def gcd3(a, b):
	assert a >= 0 and b >=0
	if a == 0 or b == 0: return max(a, b)
	elif a >= b: return gcd3(a % b, b)
	else: return gcd3(a, a % b)

def gcd4(a, b):
	assert a >= 0 and b >=0
	if a == 0 or b == 0: return max(a, b)
	return gcd4(b % a, a)

print(gcd4(4, 2))