def min(nums):
	smallest = nums[0]
	for candidate in nums:
		if(candidate < smallest):
			smallest = candidate
	return smallest

