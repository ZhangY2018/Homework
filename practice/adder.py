def add(a,b):
	c = a+b
	return c
def multiply(a,b):
	c = 0
	for x in range(a):
		print(c,"this is c")
		c = add(c,b)
	return c
def pow(a,b):
	c = 1
	for x in range(b):
		print(c,"pow")
		c = multiply(a,c)
	return c

x = pow(1,1)
z = pow(2,1)


x1 = (1**1)
x2 = (2**1)
print(x,z)
print(x1,x2)
