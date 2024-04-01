
def binary_search(numlist, n):
	leftindex = 0
	rightindex = len(numlist)-1
	while leftindex <= rightindex:
		mid = leftindex + (rightindex - leftindex) // 2
		if numlist[mid] == n:
			return mid
		elif numlist[mid] < n:
			leftindex = mid + 1
		else:
			rightindex = mid - 1
	return -1


numlist = [1, 3, 5, 8, 10, 14, 19, 21, 30]
n = 14
result = binary_search(numlist, n)
if result != -1:
	print("Found", result)
else:
	print("Not found")
