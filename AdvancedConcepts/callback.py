a = 100

def myfun():
    print("hi")

b = myfun

print(a)
print(b)
b()




def addprocessor(s):
    for i in s:
        print(i+100)

def subprocessor(s):
    for i in s:
        print(i-100)

def processNumbers(nums, processor_callback):
    processor_callback(nums)


intarry = [1,20,3,9,4]

processNumbers(intarry,addprocessor)
processNumbers(intarry,subprocessor)