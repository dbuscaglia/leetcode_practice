class Solution(object):
	def moveZeroes(self, nums):
		i = 0
		
		for x in range(len(nums)):
			if i > len(nums) - 1:
				break
			n = nums[i]
			if n == 0:
				nums.pop(i)
				nums.append(n)
			else:
				i+=1



l = [0,0,1]

print(Solution().moveZeroes(l))
print(l)