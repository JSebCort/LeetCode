'''
Problem Name: Shortest Distance to a Character
Description:
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.

EXAMPLE:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
'''
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        # Two arrays, one for the answer, one for the location of c
        answer = []
        loc = []
        
        # Finds the locations of c and appends to c
        for i in range(len(s)):
            if s[i] == c:
                loc.append(i)
                
        # Iterates through s
        for i in range(len(s)):
            # This compares every index in s to the index of every c. It finds the absolute val of the
            # difference between the incoming index and the indices of c, then the minimum of those. 
            # The minimum is appended to answer.
            answer.append(min(abs(i-j) for j in loc))
            
        return answer