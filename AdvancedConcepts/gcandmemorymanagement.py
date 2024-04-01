#gcandmemorymanagement
# import random
import gc
def leakMem ():
    i = 0
    a = []
    while ( i < 999999):
        a.append( 1 )
        i = i + 1
    print ( "here" )
#    gc.disable()

leakMem()
print("outside leakmem")
gc.collect()
print("end")



# import sys

# # Create an object
# x = [1, 2, 3]

# # Get reference count
# ref_count = sys.getrefcount(x)

# print("Reference count of x:", ref_count)
