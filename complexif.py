name = raw_input ("Enter your first name ")
password = raw_input ("Enter your password ")

if(name == "omer" and password == "dinosaur") or (name == "Zhang" and password == "9080waiwai@721") or (name == "Robin" and password == "batcave") or (name == "mo" and password == "666"):
	print("you are logged in")
else:
	print("Access denied")

if(name == "omer" or name == "Zhang" or name == "Robin"):
	print("That was a badass name~")
if(not(name == "mo")):
	print("	OK ")
else:
	print("Wait, what's your name again....")
