
def findNinMints(input,n):
    for index, integerI in enumerate(input):
        if ( integerI == n ):
            return index
    return "not found"
#ints = [2,4,5,8,9,0]
#print ( findNinMints( ints, 5) )

listofints = { 3:[21,41,15,38,29,10], 31:[21,41,15,31,38,29,10] }

for item in listofints:
    print( findNinMints( listofints[item],item) )
