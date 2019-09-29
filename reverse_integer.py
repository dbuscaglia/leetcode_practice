"""
7. Reverse Integer
Easy

2476

3842

Favorite

Share
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if x < 0:
        	s = s[1:]
        	b = ''.join(reversed(s))
        	b = "-"+b
        else:
        	b = ''.join(reversed(s))
        r = int(b)
        if r > 2147483647 or r < -2147483648:
        	return 0
        return r


assert Solution().reverse(-123) == -321
assert Solution().reverse(1234) == 4321


