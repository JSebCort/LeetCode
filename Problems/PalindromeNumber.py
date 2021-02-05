'''
Problem Name: Palindrome Number

Description: 
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

EXAMPLES:
Input: x = 121
Output: true

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        # A palindrome can't be negative, thus return False
        if x < 0:
            return False
        
        # Create a copy of the integer and reverse it
        num = [int(n) for n in str(x)]
        rev = num.copy()
        rev.reverse()
        
        # If the copy and original match, it's a palindrome
        return(num == rev)