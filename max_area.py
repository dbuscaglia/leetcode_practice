'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

 

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
class Solution(object):
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		max_height = 0
		# doing something with 2 pointers here...
		l = 0
		r = len(height) -  1

		while (l != r):
			y_l = height[l]
			y_r = height[r]

			y = min(y_r, y_l)
			x = r - l
			max_height = max(max_height, y * x)

			if y_l >= y_r:
				r -= 1
			else:
				l += 1

		return max_height

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
