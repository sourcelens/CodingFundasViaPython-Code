#1
#year = 1990
# if (year % 4) == 0:
#     if (year % 100) == 0:
#         if (year % 400) == 0:
#             print(year, " is a leap year")
#         else:
#             print(year, " is not a leap year")
#     else:
#         print(year, " is a leap year")
# else:
#     print(year, " is not a leap year")


#2
# if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
#     print("The year is a leap year!")
# else:
#     print("The year isn't a leap year!")

#3
# def leapyr(year):
#     if year % 400 == 0:
#         return True #400, 800, 1200
#     if year % 100 == 0:
#         return False # 300, 200, 100, 500,
#     if year % 4 == 0:
#         return True # 4, 8, 20, 
#     return False # 1, 2, 3, 5, 6, ...

# print (leapyr(year))


#4
def IsThisALeapYear( year ):
    #year = 2000
    if (year % 400 == 0):
        return True #print("{0} is a leap year".format(year)) # 400, 800, 1200
    elif (year % 4 ==0) and (year % 100 != 0):
        return True #print("{0} is a leap year".format(year)) # 4, 8, 12
    else:
        return False #print("{0} is not a leap year".format(year)) # 1, 2, 3, ...100, 200, 300, 
    
num = 3000
for i in range( num ):
    if IsThisALeapYear(i):
        print ( str(i) + " is a leap year")
    else:
        print ( str(i) + " is NOT a leap year")