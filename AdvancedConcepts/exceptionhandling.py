#exceptionhandling

try:
    numerator = 10
    denominator = 2

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")



#https://docs.python.org/3/library/exceptions.html
try:
    index = 10
    even_numbers = [0,2,4,6,8]
    print(10/even_numbers[index])
except ZeroDivisionError as e:
    print("Denominator cannot be 0.")
except IndexError as e:
    print("Index Out of Bound.")



even_numbers = [0,2,4,6,8]
if( index >= len(even_numbers) ):
    print("Index Out of Bound.")
elif ( 0 == even_numbers[index]):
    print("Denominator cannot be 0.")
else:
    print(10/even_numbers[index])


# program to print the reciprocal of even numbers
try:
    num = 0
    assert num % 2 == 0
except:
    print("String entered is Not an even number!")
else:
    try:
        reciprocal = 1/num
        print(reciprocal)
    except ZeroDivisionError:
        print("Sorry zero is not allowed")






try:
    numerator = 10
    denominator = 1

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

finally:
    print("This is finally block.")




def myexepfun():
    raise Exception("test")
try:
    myexepfun()
except Exception as err:
    print(err)


# define Python user-defined exceptions
class SourceLensException(Exception):
    pass

def myexepfun():
    raise SourceLensException("Very Specific Sourcelens Exception. No one knows when it generated. Reach out to SourceLens for More info")
try:
    myexepfun()
except SourceLensException as err:
    print(err)


# import sys
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')


# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")