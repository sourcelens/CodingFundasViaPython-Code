# def innerdecorfunc(inputfunc):
# 		print("Inside innerdecorfunc before inputfunc execution")
# 		inputfunc()
# 		print("Inside innerdecorfunc after inputfunc execution")
# def my_decorator():
# 	return innerdecorfunc

# def function_2b_decorated():
# 	print("Inside the function_2b_decorated")

# resultfunction = my_decorator()
# resultfunction(function_2b_decorated)




def my_decorator(inputfunc):
	def innerdecorfunc():
		print("Inside innerdecorfunc before inputfunc execution")
		inputfunc()
		print("Inside innerdecorfunc after inputfunc execution")	
	return innerdecorfunc

def function_2b_decorated():
	print("Inside the function_2b_decorated")


resultfunction = my_decorator(function_2b_decorated)
resultfunction()


def function_2b_decorated_with_no_sugar():
	print("Inside the function_2b_decorated_with_no_sugar")

@my_decorator
def anotherFunctionToBeDecoratedWithSugarOfSyntax():
	print("Inside anotherFunctionToBeDecoratedWithSugarOfSyntax")

function_2b_decorated_with_no_sugar = my_decorator(function_2b_decorated_with_no_sugar)
function_2b_decorated_with_no_sugar()

anotherFunctionToBeDecoratedWithSugarOfSyntax()

# importing libraries
# import time
# import math

# # decorator to calculate duration
# # taken by any function.
# def calculate_time(func):
	
# 	# added arguments inside the inner1,
# 	# if function takes any arguments,
# 	# can be added like this.
# 	def inner1(*args, **kwargs):

# 		# storing time before function execution
# 		begin = time.time()
		
# 		func(*args, **kwargs)

# 		# storing time after function execution
# 		end = time.time()
# 		print("Total time taken in : ", func.__name__, end - begin)

# 	return inner1



# # this can be added to any function present,
# # in this case to calculate a factorial
# @calculate_time
# def factorial(num):

# 	# sleep 2 seconds because it takes very less time
# 	# so that you can see the actual difference
# 	time.sleep(2)
# 	print(math.factorial(num))

# # calling the function.
# factorial(10)


def hello_decorator(func):
	def inner1(a,b):
		print("before Execution")
		# getting the returned value
		returned_value = func(a, b)
		print("after Execution")
		# returning the value to the original frame
		return returned_value
	return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
	print("Inside the function")
	return a + b

# getting the value through return of the function
print("Sum =", sum_two_numbers(1, 2))












# code for testing decorator chaining 
def decor1(func): 
	def inner(): 
		x = func() 
		return x * x 
	return inner 

def decor(func): 
	def inner(): 
		x = func() 
		return 2 * x 
	return inner 

@decor1
@decor
def num(): 
	return 10

@decor
@decor1
def num2():
	return 10

print(num()) 
print(num2())
