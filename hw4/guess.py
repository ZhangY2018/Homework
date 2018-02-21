
#today, change to random number
import random

answer = random.randint(0,5)

guess = int(raw_input("Enter a number, 0-5:"))

if(guess > answer):
	print("You number is too high")
	guess = int(raw_input("Enter a number, 0-5:"))
	if(guess > answer):
		print("your number is still too high")
	elif(guess < answer):
		print("your number is too low")
	elif(guess == answer):
		print("Good job! you got my number!")

elif(guess < answer):
	print("You number is too low")
elif(guess == answer):
	print("Yes, you guessed my number")


