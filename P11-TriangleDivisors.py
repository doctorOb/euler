"""What is the value of the first triangle number to have over five hundred divisors"""

from math import sqrt

def triangleNumbers(n=None):
	"""generate all triangle numbers (each a sum of the first n natural numbers)"""
	stop = 100000000 if n == None else n
	last_triangle = 0
	for i in range(1,stop):
		yield i + last_triangle
		last_triangle+=i

def divisors(num):
	"""compute the divisors of the number given by num. This is done using the divisor pair method"""
	ret = []
	for i in range(1,int(sqrt(num))):
		if num % i == 0:
			ret.append(i)
			ret.append(num / i)
	return ret

def solve():
	"""find the first triangle number with more then 500 divisors"""
	for triangle in triangleNumbers():
		if len(divisors(triangle)) > 500:
			return triangle





if __name__ == '__main__':
	print(solve())
