'''
Problem Name: The K Weakest Rows in a Matrix
Description:
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

    The number of soldiers in row i is less than the number of soldiers in row j.
    Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

EXAMPLE:
Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
'''

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Dictionary
        strength = {}
        
        # Iterates through list and adds the row index as key, number of 1s as value
        for i in range(len(mat)):
            strength[i] = mat[i].count(1)
        
        # Sorts the dictionary
        strength = dict(sorted(strength.items(), key= lambda item: item[1]))
        
        # Unpacks the dictionary as a list, slices it to the length of K and returns it
        return([*strength][0:k])