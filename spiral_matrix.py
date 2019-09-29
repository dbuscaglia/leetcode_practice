'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 0]
'''


class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if len(matrix) == 0:
			return []
		if len(matrix[0]) == 0:
			return []

		if len(matrix[0]) == 1:
			return [x[0] for x in matrix]

		x_right_boundary = len(matrix[0])
		y_bottom_boundary = len(matrix)
		x_left_boundary = 0
		y_top_boundary = 0


		x_position = 0
		y_position = 0

		result = []
		doWork = True
		while doWork and x_position >= 0 and y_position >= 0:
			doWork = False

			if x_position == x_right_boundary and y_position == y_top_boundary:
				return result

			if x_position == x_left_boundary and y_position ==  y_bottom_boundary:
				return result

			for x in range(x_position, x_right_boundary, 1):
				result.append(matrix[y_position][x])
				x_position = x
				doWork = True

			x_right_boundary -= 1
			y_top_boundary += 1

			if y_bottom_boundary >= 0 and y_top_boundary <= len(matrix):

				for y in range(y_top_boundary, y_bottom_boundary,  1):
					result.append(matrix[y][x_position])
					y_position = y
					doWork = True

			#if y_bottom_boundary -  1 != y_top_boundary - 1 and x_right_boundary > 0:
			if x_right_boundary - 1 != x_left_boundary - 1 and y_bottom_boundary >= 0:
				for x in range(x_right_boundary - 1, x_left_boundary - 1, -1):
					result.append(matrix[y_position][x])
					x_position = x
					doWork = True

			y_bottom_boundary -= 1


			if y_bottom_boundary -  1 != y_top_boundary - 1 and x_right_boundary > 0:
			#if x_right_boundary - 1 != x_left_boundary - 1 and y_bottom_boundary >= 0:
				for y in range(y_bottom_boundary -  1, y_top_boundary - 1, - 1):	
					result.append(matrix[y][x_position])
					y_position = y
					doWork = True
				
			x_left_boundary += 1
			x_position += 1

		return result

'''
assert Solution().spiralOrder(
	[
		[ 1, 2, 3 ],
		[ 4, 5, 6 ],
		[ 7, 8, 9 ]
	]) == [1,2,3,6,9,8,7,4,5]

assert Solution().spiralOrder(
	[
		[1, 2, 3, 4],
		[5, 6, 7, 8],
		[9,10,11,12]
	]) == [1,2,3,4,8,12,11,10,9,5,6,7]
'''
'''
assert Solution().spiralOrder(
	[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]) == [1,2,3,4,5,6,7,8,9,10]
'''
assert Solution().spiralOrder(

	[[2,5,8],
	[4,0,-1]]
) == [2,5,8,-1,0,4]