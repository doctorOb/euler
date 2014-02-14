import sys
sys.path.append('helpers.py')
from helpers import *
from time import sleep

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





if __name__ == '__main__':
	findPrimeFactors(600851475143)