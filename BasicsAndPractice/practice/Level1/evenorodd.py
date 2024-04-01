def isnumbereven( num ) :
   if ( 0 ==  ( num % 2 ) and ( num != 0 )):
      return True
   elif( 1 ==  ( num % 2 ) ):
      return False
   return "number is zero"

numbeloweven = 20

for i in range(numbeloweven):
   if ( True == isnumbereven(i) ):
      print ( str(i) + " Is even" )