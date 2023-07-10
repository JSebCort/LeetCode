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
    #Solition 1
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
    
    #Solution 2
    def isAnagram2(self, s: str, t: str) -> bool:
        # If t is of greater length than s, then it cannot be an anagram of s.
        if len(s) != len(t):
            return False
        
        # Create two dictionaries for each string.
        dictS, dictT = {}, {}

        # Iterate through both strings, adding +1 for every character that appears.
        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i],0)
            dictT[t[i]] = 1 + dictT.get(t[i],0)

        # If the dictionaries match in keys & values, return True.
        return dictS == dictT
