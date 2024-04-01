#for loop with nested condition inside
fruits = ["apple", "orange", "mango", "grapes"]
for f in fruits:
  if ( f == "apple"):
    print(f)


#for loop with nested for loop inside
for f in fruits:
  for n in range(0,3):
    print(str (n) + " for fruit " + f)


#for loop with nested for loop and then condition inside
for f in fruits:
  for n in range(100,103):
    if ( f == "apple"):
      print(str (n) + " just for fruit " + f + " only")