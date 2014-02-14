import math
import string

"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers."""


def isPalindrome(number):
	"""determine if the number is a palindrome"""
	original = number
	reverse = 0
	while number > 0:
		r = number % 10
		reverse = (reverse*10) + r
		number /= 10
	return original == reverse


def solve():
	"""iterate between all 3 digit numbers until largest is found"""
	largest = (0,0,0)

	for i in range(0,999):
		for j in range(0,999):
			if i % 2 == j % 2:
				product = i * j
				if isPalindrome(product) and product > largest[0]:
					largest = (product,i,j)
	print("largest palindrome is {}, the sume of {} x {}".format(*largest))
if __name__ == '__main__':
	solve();