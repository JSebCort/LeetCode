'''
Problem Name: Minimum Remove to Make Valid Parentheses
Description:
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

EXAMPLES:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack: Create a stack to hold all indices of incoming parentheses
        # valid: Holds every character of a split s
        stack = []
        valid = list(s)
        
        # Iterates through every character/index to see if its a parentheses
        for i, char in enumerate(valid):
            # If it's an open parentheses, add to the stack
            if char == '(':
                stack.append(i)
            # If it's a closing parentheses, pop from that as it'd be a match for an open parentheses
            # or simply remove the closing parentheses if there are no items in the stack
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    valid[i] = ''
                    
        # Any leftover open parentheses can also be removed as they're never close
        for i in stack:
            valid[i] = ''
            
        # Join the list into a string and return
        return "".join(valid)