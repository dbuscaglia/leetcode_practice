class Solution(object):
	def containsDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums) <= 1:
			return False

		_map = {}
		for n in nums:
			if _map.get(n):
				return True
			else:
			    _map[n] = True

		return False

	def containsNearbyDuplicate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: bool


		Given an array of integers and an integer k,
		find out whether there are two distinct
		indices i and j in the array such that
		nums[i] = nums[j]
		and the absolute difference
		between i and j is at most k.
		"""

		'''
		This times out on long Ks:

		if len(nums) <= 1:
			return False

		for i, n in enumerate(nums):
			for j in range(i + 1, i + k + 1):
				try:
					
					if n == nums[j]:
						return True
				except:
					pass
		return False
		'''

		if len(nums) <= 1:
			return False

		for i, n in enumerate(nums):
			



			

assert Solution().containsNearbyDuplicate([1,2,3,1], 3) == True
assert Solution().containsNearbyDuplicate([1,0,1,1], 1) == True
assert Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2) == False


