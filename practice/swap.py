x = int(raw_input("Enter a number"))
y = 10

print(x,y)
#swaps
def swap(first,second):
	z = first
	first = second
	second = z
	return first,second
#endswap
x,y = swap(x,y)

print(x,y)
# y = 5, x = 
