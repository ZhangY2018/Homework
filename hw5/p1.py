number = float(raw_input("Enter the reading on a thermometer "))




if(number < 96.0):
	feeling = raw_input("Are you feeling cold? ")

	if(feeling == "Yes") or (feeling == "yes") or (feeling == "YES"):
		print("~~~ Try dressing up for the winter to keep your temperature up _(:3_/ l_)_ ~~~")
	if(feeling == "No") or (feeling == "no") or (feeling == "NO"):
		print("~~~ hmph, you must be cold blooded <(O_O)> ~~~")

if(number > 99.0):
	feeling2 = raw_input("Are you feeling warm? ")

	if(feeling2 == "Yes") or (feeling2 == "yes") or (feeling2 == "YES"):
		print("~~~ Oops...You may be running a fever... :>_<: ~~~ ")
	if(feeling2 == "No") or (feeling2 == "no") or (feeling2 == "NO"):
		print("~~~ You must be warm blooded lol ~~~")

if(number == 98.6):
	print("~~~ Congratulations! You are normal and healthy ! ~~~")

else:
	print("~~~ Okey, you're healthy ~~~")
