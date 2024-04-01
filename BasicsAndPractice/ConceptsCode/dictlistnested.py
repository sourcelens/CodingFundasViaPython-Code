employdetails = {
  "name": "James Thom",
  "number": 123456,
  "Address": "Test address, NSW 1234"
}


# list
fruits = [
"mango", 
"apple", 
"tomato"
]


#list with dict and list
master1_list = [employdetails, fruits]
print(master1_list)


#list of list
veg = ['onion','tomato','radish']
master2_list = [veg, fruits]
print(master2_list)


#list of dicts
master3_list = [
                  {
                    "name": "James Thom",
                    "number": 123456,
                    "Address": "Test address, NSW 1234"
                  },

                  {
                    "name": "Charlie Laye",
                    "number": 23456,
                    "Address": "Test address, NSW 1234"
                  },
                  
                  {
                    "name": "Anita Dud",
                    "number": 4567,
                    "Address": "Test address, NSW 1234"
                  }
              ]
print(master3_list)

#dict of list
master4_dict = {
    "key1": master1_list, 
    "key2": master2_list, 
    "key3": master3_list, 
    "key4": "something else this can be another dict or list or anyother variable" }
print(master4_dict)
