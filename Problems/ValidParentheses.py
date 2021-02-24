'''
Problem Name: Valid Parentheses
Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

EXAMPLES:
Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
		# Variables to hold the stack and a dictionary which holds keys/values that correspond to matching open/close parentheses
        stack = []
        test = {'{':'}',
                '[':']',
                '(':')'}
		
		# Iterate through the string s
        for i in s:
		
			# If you encounter an opening parentheses, add to stack
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            # If you encounter a closing parentheses and it matches the last opening parentheses, remove the top of the stack
            elif len(stack) != 0 and i == test[stack[-1]]:
                stack.pop()
			
			# If the closing brackets dont match the previous opening brackets, return false. 
			# Problem rules: Open brackets must be closed in the correct order.
            else:
                return False
        
		# If we finish the loop but have leftover brackets in the stack, then it is False since all brackets need to be closed.
        if stack:
            return False
        else:
            return True