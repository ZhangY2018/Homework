import min
import random

numbers = [random.randint(1,999) for x in range (100)]

print(min0.min0(numbers))

ordered = []
while(len(numbers) > 0):
	smallest = min.min(numbers)
	ordered.append(smallest)
	numbers.remove(smallest)
print(ordered)
