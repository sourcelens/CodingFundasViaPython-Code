import sys
import os

#print(os.environ)
operation = os.environ.get('OPERATION') 

if ( None == operation):
    print ( "You need to set env var OPERATION to either +,-,/,* for this application")

#print( "Below is command line args we got" )
#print ( sys.argv )
if( len( sys.argv) != 3 ):
    print( "You need 2 arguments for this calculator")

def add(x,y):
    print(x+y)

def subtract(x,y):
    print(x-y)

def multiply(x,y):
    print(x*y)

def divide(x,y):
    print(x/y)

n1=sys.argv[1]
n2=sys.argv[2]


#op=input() 
op = operation

try:
    if op=='+':
        add(int(n1),int(n2))
    elif op=='-':
        subtract(int(n1),int(n2))
    elif op=='*':
        multiply(int(n1),int(n2))
    elif op=='/':
        divide(int(n1),int(n2))
    else:
        print("Unsupported operation")
except ValueError:
    print( "Both arguments must be String")
finally:
    print( "Calulator is exiting. Hope you enjoyed the So-fish-tication <|=|x Bye")