

# def factorial_func(n):
#     if n == 1:
#         return 1
#     else:
#         return (n * factorial_func(n-1))
    
# factorial_recur = factorial_func(num)
# print(factorial_recur)




num = 7

factorial = 1
for i in range(1, num+1):
    factorial = i * factorial
print(factorial)