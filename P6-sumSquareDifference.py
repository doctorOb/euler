import math

def sumSquare(start,stop):
	return reduce(lambda x,y: x + y,map(lambda x: x**2, range(start,stop+1)))
def squareSum(start,stop):
	return reduce(lambda x,y: x + y, range(start,stop+1))**2


if __name__ == '__main__':
	print(squareSum(1,10) - sumSquare(1,10))
	print(squareSum(1,100) - sumSquare(1,100))