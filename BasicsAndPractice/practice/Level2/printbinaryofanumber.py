def dec2bin(number):
	ans = ""
	if ( number == 0 ):
		return 0
	while ( number ):
		ans = str(number & 1) + ans 
		number = number >> 1
	return ans

number = 60
print(f"The binary of the number {number} is {dec2bin(number)}")
