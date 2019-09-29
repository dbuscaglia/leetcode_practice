MAX_INT = 2147483647
MIN_INT = -2147483648


class Solution(object):
	def myAtoi(self, s):
		"""
		:type str: str
		:rtype: int
		"""


		s = s.lstrip()
		if len(s) == 0:
			return 0

		digits = []
		fc = s[0]
		if fc == "-":
			digits.append("-")
			s = s[1:]

		if fc == "+":
			s = s[1:]

		try:
			fc = int(s[0])
		except:
			return 0

		for c in s:
			try:
				digits.append(str(int(c)))
			except ValueError:
				break

		try:
			r = int(''.join(digits))
			if r > MAX_INT:
				return MAX_INT
			if r < MIN_INT:
				return MIN_INT
			
			return r
		except ValueError:
			return 0




assert Solution().myAtoi("   -42") == -42
assert Solution().myAtoi("3.14") == 3
assert Solution().myAtoi("+1") == 1
assert Solution().myAtoi(" ") == 0
