'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''

keypad_map = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    3: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}


class Solution(object):


	def backtrack(self, c, digits, result):
		if digits is None:
			result.add(c)
			return result

		


        return []

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        output = []
        if digits is None:
        	return []
        return self.backtrack('', digits, output)



print (Solution().letterCombinations("12"))