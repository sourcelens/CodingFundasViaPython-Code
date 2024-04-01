
testvariable = 10

def function1():
    print("Inside function1")
    # print ( testvariable )
    testvariable = 1000
    print ( testvariable )

    for i in range(2):
        print ( testvariable )
        testvariable = 2000
        print ( testvariable )
        if (i == 1):
            print ( testvariable )
            testvariable = 3000
            print ( testvariable )
        print ( testvariable ) 
    print ( testvariable )
    print("Done with function1")


def function2(): 
    print("Inside function2")
    for i in range(2):
        if (i == 0):
            testvariable = 3000
            print ( testvariable )
        print ( testvariable ) 
    print ( testvariable )
    print("Done with function2")

function1()
print ( testvariable ) 
function2()
print ( testvariable ) 

