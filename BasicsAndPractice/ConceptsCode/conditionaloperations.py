#Simple if condition check
raintoday = 1
temperature = 30
humidity = 90

if ( temperature != 30 and humidity > 90):
    print("something is happening")


if ( temperature != 30):
    if ( humidity > 90):
        print("something is happening")