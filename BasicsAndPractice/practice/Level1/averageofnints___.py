
def avgfun( intarray ):
    sum = 0
    for num in intarray:
        sum = sum + num
    average = sum / len(intarray)
    return average

dictofNums = { "list1" : [2,5,1,9,20], "list2ishere": [23,53,13,93,203], "testishere": [231,531,113,203] }

for item in dictofNums:
    print ( "The avg of item " + item + " is " + str ( avgfun( dictofNums[item] ) ) )



