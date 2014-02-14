import math

matrix = []
matrix.append(map(lambda x: int(x),list("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08".split(' '))))
matrix.append(map(lambda x: int(x),list("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00".split(' '))))
matrix.append(map(lambda x: int(x),list("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65".split(' '))))
matrix.append(map(lambda x: int(x),list("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91".split(' '))))
matrix.append(map(lambda x: int(x),list("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80".split(' '))))
matrix.append(map(lambda x: int(x),list("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50".split(' '))))
matrix.append(map(lambda x: int(x),list("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70".split(' '))))
matrix.append(map(lambda x: int(x),list("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21".split(' '))))
matrix.append(map(lambda x: int(x),list("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72".split(' '))))
matrix.append(map(lambda x: int(x),list("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95".split(' '))))
matrix.append(map(lambda x: int(x),list("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92".split(' '))))
matrix.append(map(lambda x: int(x),list("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57".split(' '))))
matrix.append(map(lambda x: int(x),list("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58".split(' '))))
matrix.append(map(lambda x: int(x),list("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40".split(' '))))
matrix.append(map(lambda x: int(x),list("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66".split(' '))))
matrix.append(map(lambda x: int(x),list("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69".split(' '))))
matrix.append(map(lambda x: int(x),list("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36".split(' '))))
matrix.append(map(lambda x: int(x),list("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16".split(' '))))
matrix.append(map(lambda x: int(x),list("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54".split(' '))))
matrix.append(map(lambda x: int(x),list("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48".split(' '))))



def sliceMatrix(mat,start,end):
	"""given a list of elements, give a 2d split from start to end
		@start a x,y pair to start at
		@end a x,y pair to end at"""
	ret = []
	for i in range(start[0],end[0]):
		row = []
		for j in range(start[1],end[1]):
			row.append(mat[i][j])
		ret.append(row)
	return ret

def sumMatrix(mat):
	"""sum the (assumed int) elements in a matrix"""
	s = 0
	for row in range(0,len(mat) - 1):
		s += sum(mat[row])
	return s

def diagonals(mat,minLen=4):

	dim = len(mat)
	slice = dim*2 - 2
	diagonals = []

	#get the diagonals in the right ascending direction
	while slice >= 0:
		z = 0 if slice < dim else slice - dim + 1
		j = slice - z
		row = []
		while j >= z:
			row.append(mat[j][slice - j])
			j-=1

		if len(row) >= minLen:
				yield row
		slice-=1

	#get diagonals from the left ascending direction
	slice = 0
	while slice < dim*2 - 1:
		z = 0 if slice < dim else slice - dim + 1
		j = slice - z
		row = []
		while j >= z:
			row.append(mat[j][slice - j])
			j-=1

		if len(row) >= minLen:
			yield row
		slice+=1




def product(list):
	"""return the product of all numbers in the list"""
	return reduce(lambda x,y: x*y,list)

def findMaxProduct(mat):
	"""find the largest product of 4 consecutive digits 
	in the mat of boxSize"""
	largest = 0
	for line in verticals(matrix):
		check = maxSum(line)
		if check > largest:
			largest = check

	for line in horizontals(matrix):
		check = maxSum(line)
		if check > largest:
			largest = check		

	for line in diagonals(matrix):
		check = maxSum(line)
		if check > largest:
			largest = check

	return largest


def verticals(mat):
	for x in range(0,len(mat)):
		ret = []
		for y in range(0,len(mat)):
			ret.append(mat[y][x])
		yield ret

def horizontals(mat):
	for row in mat:
		yield row


def maxSum(mat,n=4):
	m = 0
	for i in range(0,len(mat) - n + 1):
		next = reduce(lambda x,y: x*y, mat[i:i+n])
		if next > m:
			m = next

	return m



	



if __name__ == '__main__':
	topLeft = sliceMatrix(matrix,(0,0),(5,5))
	print(findMaxProduct(matrix))




