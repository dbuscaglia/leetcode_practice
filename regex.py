class Fragment:
	def __init__(self, start, stop, substring):
		self.start = start
		self.stop = stop
		self.substring = substring


class Dot:
	def __init__(self):
		pass

	def __str__(self):
		return "|Dot|"

	def __repr__(self):
		return self.__str__()

class Star:
	def __init__(self, char):
		self.char = char

	def __str__(self):
		return "|*({})|".format(self.char)

	def __repr__(self):
		return self.__str__()

class Char:
	def __init__(self, char):
		self.char = char

	def __str__(self):
		return "|{}|".format(self.char)

	def __repr__(self):
		return self.__str__()

class RegTree:

	badPrefixChars = ['', '*']

	def __init__(self, s, p):
		self.badParse = False
		self.hasExotic = False
		self._parse(s, p)


	def _parse(self, s, p):
		self.tree = []
		lastletter = ''
		i = 0
		letters_to_remove = []
		print (s)
		for c in p:
			if c == ".":
				self.tree.append(Dot())
				self.hasExotic = True
				lastletter = '.'
			elif c == "*":
				if lastletter in self.badPrefixChars:
					self.badParse = True

				self.tree.append(Star(lastletter))
				self.hasExotic = True
				letters_to_remove.append(i)
				lastletter = '*'
			else:
				self.tree.append(Char(c))
				lastletter = c
			i += 1

		for i, pos in enumerate(letters_to_remove):
			mod_pos = pos - i
			s = s[:mod_pos] + s[(mod_pos+1):]

		self.simplified_string = s
		print (self.simplified_string)

	def __str__(self):
		return ''.join([str(s) for s in self.tree])

	def __repr__(self):
		return self.__str__()

	def __iter__(self):
		return iter(self.tree)


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.tree = RegTree(s, p)
        if self.tree.badParse:
        	return False

        if not self.tree.hasExotic:
        	return s == p
        else:
        	return self._parseExotic(self.tree.simplified_string, p)

    def _parseExotic(self, s, p):
    	i = 0
    	for token in self.tree:
    		if isinstance(token, Char):
    			if s[i] != token.char:
    				return False
    			else:
    				i += 1
    		elif isinstance (token, Star):

    			if s[i] != token.char and token.char != '*':
    				i += 1
    			elif s[i] != token.char and token.char == '*':
    				i += 1
    			else:
    				for x in range(i, len(s)):
    					if s[i] != token.char and token.char != '*':
    						i = x
    						break;

    		elif isinstance(token, Dot):
    			try:
    				letter = s[i]
    				i += 1
    			except:
    				print ("weird no dot")
    				return False

    		else:
    			print ("hmmmm")
    			return False

    		if i >= len(s):
    			return True


    	return True


"""
Given an input string (s) and a pattern (p), implement regular expression matching
with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
"""



#assert Solution().isMatch("aa", "a") is False                   # false
#assert Solution().isMatch("aa", "a*") is True                   # true
#assert Solution().isMatch("ab", ".*") is True                   # true
assert Solution().isMatch("aab", "c*a*b") is True               # true
assert Solution().isMatch("mississippi", "mis*is*p*.") is False # false


