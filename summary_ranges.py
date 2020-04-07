class Solution(object):
	def summaryRanges(self, nums):
		"""
		Given a sorted integer array without duplicates, return the summary of its ranges.
		:type nums: List[int]
		:rtype: List[str]

		Input:  [0,1,2,4,5,7]
		Output: ["0->2","4->5","7"]
		Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
		"""
		c = 0
		rangeStart = None
		rangeNext = None
		if nums == []:
			return []
		result = []
		for i, n in enumerate(nums):
			if rangeStart == None:
				rangeStart = n
				rangeNext = n
				continue
			rangePrevious = rangeNext
			rangeNext += 1

			if n != rangeNext:
				if rangePrevious == rangeStart:
					result.append("{}".format(rangeStart))
				else:
					result.append("{}->{}".format(rangeStart, rangePrevious))

				rangeStart = n
				rangePrevious = n
				rangeNext = n


		if rangeStart == rangeNext:
			result.append("{}".format(rangeStart))
		else:
			result.append("{}->{}".format(rangeStart, rangeNext))

		return result










l = [0,1,2,4,5,7]
o = ["0->2", "4->5", "7"]

print Solution().summaryRanges(l)
#assert o == Solution().summaryRanges(l)