a = 10
b = 20

temp = b
b = a
a = temp

print ( a )
print ( b )

#trick no temp var, not generic... what if a and b are strings?
b = a+b
a = b-a
b = b-a

print ( a )
print ( b )

#see below to understand the problem, take ur interviewer for a ride.
teststr1 = "apple"
teststr2 = "mango"
#print(teststr1-teststr2)

temp = teststr1
teststr1 = teststr2
teststr2 = temp

print ( teststr1 )
print ( teststr2 )