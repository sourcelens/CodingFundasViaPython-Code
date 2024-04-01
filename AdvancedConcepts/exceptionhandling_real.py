dict1 = { "dog":"boblie", "cat":"dablu"}

print ( dict1['rabit'])

if 'rabit' in dict1:
    print(dict1['rabit'])
else:
    print( "We have no rabits")

try:
    print(dict1['rabit'])
except:
    print( "We have no rabits")