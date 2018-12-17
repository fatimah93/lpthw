def function_name(testing):
	
	i = 1 
	numbers = []

	while i < testing: 
		print(f"At the top i is {i}")
		numbers.append(i)

		i = i + 1
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {i}")
	return numbers
numbers = function_name(6)

print("The numbers: ")

for num in numbers:
	print(num)







