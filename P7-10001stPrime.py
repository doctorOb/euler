"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?"""
import sys
sys.path.append('helpers.py')
from helpers import isPrime


def getPrime(n):
	"""find the nth prime number"""
	primeCount = 0
	i = 0
	while primeCount != n:
		i+=1
		if isPrime(i):
			primeCount+=1
			print("{} prime number is {}".format(primeCount,i))
	return i


if __name__ == '__main__':
	print(getPrime(6))
	print(getPrime(10001))
