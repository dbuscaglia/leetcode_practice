class Solution(object):
    def removeElement(self, nums, val):
		i = 0
		while i != len(nums):
			if i > len(nums) - 1:
				break
			n = nums[i]
			if n == val:
				nums.pop(i)
			else:
				i+=1
		return len(nums)


l = [3,2,2,3]
print(Solution().removeElement(l, 3))