import swap

ten=10
fifteen=15
print(ten,fifteen)
print(swap.swap(ten,fifteen))

nums = [4,1,8,3,2]
print(nums)
x = 0
while(x < len(nums)):
	print(x,nums[x])
	x = x + 1
	if(x+1 < len(nums)):
		if(nums[0]>nums[1]):
			nums[x],nums[x+1] = swap.swap(nums[x],nums[x+1])
			x = 0
	x = x+1
print(nums)
