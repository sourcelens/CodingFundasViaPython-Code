# #break in for loop
# for count in range(0,10):
#     if (count  == 7):
#         print ( "im here this is 7")
#         continue
#     print("not broken so printing count = " + str(count) )

# # break in while loop
# i = 5
# while i <= 15:
#     print(i)
#     i = i + 1
#     if i >= 9:
#         continue   
    

# #continue in for loop
# for i in range(20):
#     if i == 12:
#         print ( """Count is 12 so going to continue the loop
#                 and no further statements will be 
#                 executed in this iteration of loop.
#                 Loop will restart from next iteration""")
#         continue
#     print(i)


# #continue in while loop
# count = 0
# while count < 20:
#     count = count + 1    
#     if count == 12:
#         continue
#     print(count)


# #return in for loop
# def function1():
#     print("Inside function1")
#     #return
#     print("Done with function1")

# #return in for loop
# def function2():
#     print("Inside function2")
#     for i in range(20):
#         if i == 12:
#             print ( "Count is 12 so going return")
#             break
#         print(i)
#     print("Done with function2")

# #return in while loop
# def function3():
#     print("Inside function3")
#     count = 0
#     while count < 20:
#         count = count + 1    
#         if (count) == 12:
#             return
#         print(count)
#     print("Done with function3")


#return in for loop
def function4():
    print("Inside function4")
    count = 0
    while count < 20:
        count = count + 1    
        if (count) == 12:
            print( "Going to run inner for loop")
            for i in range(20):                
                if i == 14:
                    print ( "Count is 14 so going return")
                    continue
                print(i)
        print(count)
    print("Done with function4")


# function1()
# function2()
# function3()
return_test = function4()
print( return_test)