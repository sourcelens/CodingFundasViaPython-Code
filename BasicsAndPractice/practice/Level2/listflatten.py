
listtoflatten = [
	1, 2, 
	[
		3, 4, 
		[
			5, 6
		], 
		7
  	],
	[
		[
			[
				8, 9
			], 
			10
		]
	],
	[
		11, 
		[12, 13]
	]
]

def flatten(input_list):
	result = []
	while input_list:
		current = input_list.pop()
		if isinstance(current, list):
			input_list.extend(current)
		else:
			result.append(current)
	result.reverse()
	return result
ans = flatten(listtoflatten)
print(ans)
