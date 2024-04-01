def is_sum_even(number):
  sum = 0
  while number > 0:
    sum = sum + number % 10
    number = number // 10

  if sum % 2 == 0:
    return True
  else:
    return False

number = 454534
if ( True == is_sum_even(number) ):
  print("The sum of the digits of", number, "is even.")
else:
  print("The sum of the digits of", number, "is not even.")
