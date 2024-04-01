
def binary_search(numlist, n):
	if ( numlist == [] ):
		return [n]	
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
	if( numlist[mid] > n):
			numlist.insert( mid, n)
	else:
			numlist.insert( mid + 1, n)
	return numlist

def binary_sort( numberstosort ):
	sortedlist = []
	for n in numberstosort :
		sortedlist = binary_search( sortedlist, n )
	return sortedlist

numlist = [2,1]
result = binary_sort(numlist)
print( result )
