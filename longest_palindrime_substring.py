'''
5. Longest Palindromic Substring
Medium

4336

396

Favorite

Share
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
import math


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        current_longest = ""
        # idea: start in middle and go both ways
        floor_middle = math.floor(len(s) / 2)
        breakpoint()
        return "bab"



assert Solution().longestPalindrome("babada") == "bab"