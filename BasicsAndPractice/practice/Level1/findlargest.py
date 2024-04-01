
def myMax(list1):
	max = list1[0]
	for x in list1:
		if x > max:
			max = x
	return max

list1 = [10, 20, 4, 45, 99]
#print("Largest element is:", myMax(list1))

mylistoflist = [[101, 220, 43, 1445, 929],[120, 230, 47, 485, 969]]

count = 0
bigmax = 0
for item in mylistoflist:
	x = myMax(item)
	if x > bigmax:
		bigmax = x
	count = count + 1
	print("The max of list " + str (count) + " is " + str(x))

print(bigmax)