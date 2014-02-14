import math
import random

K_THRESH = 5

HUNDRED = 100
THOUSAND = 1000
MILLION = 1000000
BILLION = 1000000000

def fibn(n):
	"""compute the nth fibonaci number using Binet's formula"""
	return int(round(((1.618**n) - (1 - (1.618**n)) ) / math.sqrt(5)))

def coords(width,height):
	"""produce a generator of x,y coordinate pairs within the width, height bounds"""
	for y in range(height):
		for x in range(width):
			yield x,y

def evens(stream):
	"""iterate over a stream of integers and return the even values"""
	for value in stream:
		if values % 2 == 0:
			yield value

def odds(stream):
	"""iterate over a stream of integers and return the odd values"""
	for value in stream:
		if values % 2 != 0:
			yield value

def powerMod(a,b,c):
	"""powermod of a,b,c"""
	if b == 0:
		return 1
	if b % 2 == 0:
		return powerMod((a*a)%c,b/2,c) % c
	else:
		return (a*powerMod(a,b-1,c)) % c

def isStrongPseudoPrime(n, a):
	s = 0
	d = n-1
	while d % 2 == 0:
		d = d / 2
		s = s + 1
	t = powerMod(a,d,n)
	if t == 1:
		return True
	while s > 0:
		if t == n - 1:
			return True
		t = (t * t) % n
		s = s - 1
	return False

def isPrime(n):
	"""determine if the given number is a prime, probabilisticly
	using the Miller-Rabin primality test"""

	if n == 2:
		return True

	# ensure n is odd, and non zero
	if n % 2 == 0 or n < 2:
		return False

	for i in range(1,K_THRESH):
		a = random.randint(2, n-1)
		if not isStrongPseudoPrime(n, a):
			return False 
	return True

def isPalindrome(number):
	"""determine if the number is a palindrome"""
	original = number
	reverse = 0
	while number > 0:
		r = number % 10
		reverse = (reverse*10) + r
		number /= 10
	return original == reverse

def findPrimeFactors(n):
	"""compute the prime factorization of n, 
	return them as an array"""
	i = 2
	primes = []

	while not isPrime(n):
		if not isPrime(i):
			i = i + 1#not a prime, continue
			continue
		quot,rem = divmod(n,i)
		if rem == 0:
			n = quot
			primes.append(i)
		else:
			i = i + 1 #not divisible, continue
	primes.append(n)

	return primes

def getPrimes(n):
	"""get all the prime numberes below n, as an array"""
	i = 0
	primes = []

	while i < n:
		if isPrime(i):
			primes.append(i)
		i+=1
	return primes
		