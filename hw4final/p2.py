name = raw_input("Enter you first, middle, and the last name. ")

upper_name = name.upper()
print(upper_name)

name1 = " ".join(word[::-1] for word in name.split())
print(name1)

names = name.split()
first = names[0]
middle = names[1]
last = names[2]
final = len(middle)/2

midfir = middle[0:middlename:final+1]

finalname = (first + " " + midfir + "-BOB-" + midlas + " " + last)

print(finalname)
