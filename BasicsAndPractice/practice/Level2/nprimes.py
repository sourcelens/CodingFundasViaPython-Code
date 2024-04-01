num = 100
for n in range(1,num):
    isBroken = False
    for i in range(2, n):
        if( n % i == 0):
            isBroken = True
            break
    if ( False == isBroken ):
        print(n)

