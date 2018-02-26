PURPLE = '\033[95m'
BULE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[m'

grade = float(raw_input("Enter the grade you got on a quiz "))
#todo fill in + and + 's
if(grade >= 90.0):
	print(BULE+"you got an A !")
if(grade >= 80.0 and grade < 90.0):
	print(GREEN+"you got a B .")
if(grade >= 70.0 and grade < 80.0):
	print(YELLOW+"you got a C ...")
if(grade >=60.0 and grade < 70.0):
	print(RED+"you got a D..... :>_<:")
if(grade >=0.0 and grade < 60.0):
	print(RESET+" .... hehe ....")
