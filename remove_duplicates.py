
class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		x = 0
		i = 0
		while i != len(nums):
			if i > len(nums) - 1:
				break
			n = nums[i]
			if i == 0:
				x = n
				i+=1
				continue

			if n == x:
				nums.pop(i)
			else:
				x = n
				i+=1
		return len(nums)

l = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(l))
print(l)