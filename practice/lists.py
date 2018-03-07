socks="socks"
jeans="jeans"
laptop="laptop"
toiletries="toiletries"

luggage=[]

done="n"
while(done != "n"):
	iteml=raw_input("what you like to pack? ")
	luggage.append(iteml)
	done=raw_input("add another item? y/n")

for items in luggage:
	print(items.upper())



print(luggage[-1])

grades=[
96.0,
100.0,
75.5,
89.5
]

sum=0

for grade in grades:
	sum = sum + grade
	print(sum)
