

print("Before All functions")

#simple function
def function1():
    print("Inside function1")

#function retruns a value
def function2():
    print("Inside function2")
    return "This is returned from function"


#function with returns value and take arguments
def function3(input1, input2):
    print("Inside function3")
    return_value = input1 + input2
    return return_value

function1()
return_val_from_function = function2()
print( return_val_from_function )

return_val_from_function = function3(2, 3)
print( return_val_from_function )

return_val_from_function = function3("hello", "test")
print( return_val_from_function )

print("After All functions")