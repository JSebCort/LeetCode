'''
Problem Name: Group Anagrams
Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

------------------------------------
EXAMPLES:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation: Both s and t become "ac".

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Check if the strs list is empty
        if not strs:
            return [""]

        #Creates a defaultdict to handle an edge case 
        ans = defaultdict(list)

        #Iterate through every string inside strs
        for i in strs:

            #Create a list of 26 0s, with each 0 pertaining to a letter in the alphabet
            #Ex) [a,b,c,d,e] => [0,0,0,0,0]
            count = [0] * 26

            #Iterate through every character of the string
            for j in i:
                #Add 1 to the list of 0s if the character appears in the string
                #Ex) bed => [0,1,0,1,1]
                count[ord(j)-97] += 1 #Alternatively: count[ord(c) - ord('a')] += 1
            
            #Using the list of 0s as the key, append the string to the list of values corresponding to that key.
            #Ex) bed & deb => [0,1,0,1,1]: [bed, deb]
            ans[tuple(count)].append(i)

        return(ans.values())