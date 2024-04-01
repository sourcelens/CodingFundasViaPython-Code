
def vowel_count(input_str):
	count = 0
	vowels = "aeiouAEIOU"
	for character in input_str:
		for vowel in vowels:
			if character == vowel:
				count = count + 1
				break
	print("count = ", count)
str = "SourceLens is a Training and Consulting company"
vowel_count(str)