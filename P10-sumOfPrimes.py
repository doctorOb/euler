import sys
sys.path.append('helpers.py')
from helpers import *
import sys

def primeSieve(n):
	"""calculate all prime numbers below n, using the sieve of Eratosthenes"""
	a = [True] * n
	a[0] = a[1] = False

	for (i,prime) in enumerate(a):
		if prime:
			yield i
			for i in range(i*i,n,i):
				a[i] = False



if __name__ == '__main__':

	
	print(sum(primeSieve(2*MILLION)))
	