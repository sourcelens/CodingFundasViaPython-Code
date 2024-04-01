def triangle(levels):
	decreasingcounter = levels
	for increasingcounter in range(0, levels):
		decreasingcounter = decreasingcounter - 1
		for i in range(0, decreasingcounter):
			print(end=" ")
		for i in range(0, increasingcounter + 1):
			print("* ", end="")
		print("\r")

levels = 3
triangle(levels)
