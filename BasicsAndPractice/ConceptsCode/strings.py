string_variable = "this is a string"

for i in string_variable:
    print (i)


print(string_variable[0])

print(string_variable[len(string_variable)-1])

another_string = "another one here"
concatinatedstring = string_variable + " " + another_string
print( concatinatedstring )


index = string_variable.find('a')
print ( index )



string = "Puppys are dragons without fire"
string = string.replace("Puppys", "Kitties")
print(string)
string = string.replace("dragons", "cuties")
print(string)

splitedstringlist = string_variable.split("s")
for i in splitedstringlist:
    print(i)




