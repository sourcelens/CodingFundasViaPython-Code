def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
stringone = "String to reverse"
print(stringone)
print(reverse(stringone))


stringtwo = "This is another string to reverse"
print ( stringtwo )
print ( stringtwo[::-1])


