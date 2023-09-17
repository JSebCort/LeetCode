'''
Problem Name: Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
------------------------------------
EXAMPLES:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Check if string length is either 1 or 0
        if (len(s) <= 1):
            return True
        
        #User regular expression to remove all the non-alphanumberic characters.
        ans = re.sub('[\W_]','',s).lower()

        #Check and return if the string's slice in reverse matches the string.
        return(ans[::-1] == ans)