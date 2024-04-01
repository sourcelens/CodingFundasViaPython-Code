testvariable = 10 # Scope global

def function1():
    print("Inside function1")
    global testvariable
    print ( testvariable )
    testvariable = 1000 #local
    print ( testvariable )


def function2():
    print("Inside function2")
    global testvariable
    print ( testvariable )
    testvariable = 2000 #global
    print ( testvariable )

function1()
function2()
print ( testvariable )