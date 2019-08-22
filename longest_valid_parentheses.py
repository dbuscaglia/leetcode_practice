'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
    	paren_stack = Stack()
    	paren_stack.push(-1)
    	max_len = 0
    	for i, char in enumerate(s):
    		if char == "(":
    			paren_stack.push(i)
    		else:
    			l = paren_stack.pop()
    			if paren_stack.isEmpty():
    				paren_stack.push(i)
    			else:
    				max_len = max(max_len, i - paren_stack.peek())
    	return max_len



#print(Solution().longestValidParentheses("(()") )
assert Solution().longestValidParentheses("(()") == 2
assert Solution().longestValidParentheses(")()())") == 4

