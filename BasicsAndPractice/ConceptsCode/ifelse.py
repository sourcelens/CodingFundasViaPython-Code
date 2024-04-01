#Simple if condition check
raintoday = 1
# if ( raintoday >= 1 ) :
#     print("Take umberlla")


#if with else
# if ( raintoday == 0 ):
#     print( "lets play soccer")
# else:
#     print( "lets play pingpong")

# if with else and if-else .. else
indoor_badminton_court = False
tennis_court_is_booked = True
if ( raintoday == 1 ):
    print ( "Rain is there we need to play indoor games")
    if ( indoor_badminton_court == True):
        print("lets play badminton")
    else:
        print("lets play chess")
elif (tennis_court_is_booked == True) :
    print("lets play tennis")
else:
    print("lets go for jogging")

temperature = 25
humidity = 90

if ( temperature != 25 and humidity > 80 ) :
    print("There will be rain today")
