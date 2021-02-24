'''
Problem Name: Valid Anagram
Description: Given two strings s and t , write a function to determine if t is an anagram of s.

EXAMPLES:
Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "rat", t = "car"
Output: false
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If t is of greater length than s, then it cannot be an anagram of s.
        if len(t) != len(s):
            return False
        
        # Create a dictionary of s, which holds the occurrence of every letter 
        word = {}
        for i in s:
            word[i] = word.get(i,0)+1
        
        # Iterate through t, subtracting every occurance of a letter from the dictionary.
        # If a letter exists in t but not s, it cannot be an anagram of s.
        for i in t:
            if i in word:
                if word.get(i) > 0:
                    word[i] = word[i]-1
            else:
                return False
            
        # Return whether all values in the dictionary are 0. This would mean that
        # all letter occurances were used in t.
        return all(value==0 for value in word.values())