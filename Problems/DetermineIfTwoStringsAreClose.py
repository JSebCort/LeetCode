'''
Problem Name: Determine if Two Strings Are Close

Description:
Two strings are considered close if you can attain one from the other using the following operations:

    Operation 1: Swap any two existing characters.
        For example, abcde -> aecdb
    Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
        For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

EXAMPLE
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
'''

import collections
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check length
        if len(word1) != len(word2):
            return False
        
		# Create Dictionaries
        d1 = {}
        d2 = {}
        for i in word1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] = d1[i]+1
        
        for i in word2:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] = d2[i]+1
        
        # Check Keys
        if set(d1.keys()) != set(d2.keys()):
            return False
        
        vals1 = d1.values()
        vals2 = d2.values()
        
        # Check Values
        return(collections.Counter(vals1) ==  collections.Counter(vals2))
