loopCount=10
index=0
while(index < loopCount):
	print(index)
	index = index + 1


quit = ""

while(quit != "q"):
	print("Press q to quit")
	quit = raw_input(">")


secret = 7
number = 0
name = ""

while(number != secret and name.lower() == "Zhang"):
	print("What is your name? ")
	name = int(raw_input(">"))
	print("Guese my number between 0 and 10")
	number = int(raw_input(">"))
	if(number < secret):
		print("your number is too low")
	elif(number > secret):
		print("your number is too high")

