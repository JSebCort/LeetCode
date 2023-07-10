'''
Problem Name: Backspace String Compare
Description:
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

------------------------------------
EXAMPLES:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
'''
class Solution:                
    def backspaceCompare(self, s: str, t: str) -> bool:
	
		# Function to handle the string as if it were typed.
        def newFunction(string):
			# Creates an empty list to store the final string.
            lst = []
			
			# For loop that iterates over the input string.
            for i in string:
				# If the input is a character, append it to list.
                if i != '#':
                    lst.append(i)
				# Else, pop out the recent character as it would've been backspaced.
                elif i == '#' and len(lst) > 0:
                    lst.pop()
					
			# Return the final list.
            return lst
        
		# Returns True or False if two lists are the same
        return newFunction(s) == newFunction(t)