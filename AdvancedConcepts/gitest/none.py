#none

# The None keyword is used to define a null value, or no value at all.
# None is not the same as 0, False, or an empty string. None is a data type of its own (NoneType) and only None can be None

x = None

if x:
  print("Do you think None is True? Nope its not")
elif x is False:
  print ("Do you think None is False?")
else:
  print("None is not True, or False, None is just None...")