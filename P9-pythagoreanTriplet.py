"""There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc."""

import math



def isPythagoreanTriplet(a,b,c):
	"""determine if a < b < c and a^2 + b^2 = c^2
	formally, a Pythagorean triplet"""
	if a < b and b < c:
		return (a**2 + b**2) == c**2
	else:
		return False


def solve(n):
	"""n = a + b + c, where a,b,c are a pythagorean triplet"""
	for a in range(1,n):
		for b in range(a,n):
			for c in range(b,n):
				if a + b + c == 1000 and isPythagoreanTriplet(a,b,c):
					return (a,b,c)






if __name__ == '__main__':
	print("{} tiplet? {}".format((3,4,5),isPythagoreanTriplet(3,4,5)))
	ans = solve(1000)
	print(ans)
	sum = reduce(lambda x,y: x*y,ans)
	print("{}".format(sum))