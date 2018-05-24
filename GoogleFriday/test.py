
score = 0

print "welcome to Health Cooking Competition!".center(60)


def Choice(options):
	if options == "1":return 10
	elif options == "2":return 5
	elif options == "3":return 1
	else:return 0


while True:
	sum=raw_input("""Choose your ingredients, type the options:
1:cucumber
2:banana
3:Durian""")
	if not Choice(sum):continue
	score += Choice(sum)
	sum=raw_input("""Then, choose your seasoning:
1:soy sause
2:vinegar
3:salt""")
	if not Choice(sum):continue
	score += Choice(sum)
	sum=raw_input("""Choose your cooking method:
1:steam
2:dirt fry
3:deep fry""")
	if not Choice(sum):continue
	score += Choice(sum)
	sum=raw_input("""Choose your cooking time:
1:30min
2:10min
3:12hrs""")
	if not Choice(sum):continue
	score += Choice(sum)


print "Your health cooking score is:",score
