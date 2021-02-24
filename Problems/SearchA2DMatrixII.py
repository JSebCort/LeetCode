'''
Problem Name:  Search a 2D Matrix II
Description:
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

EXAMPLES:
			[1,4,7,11,15]
			[2,->5<-,8,12,19]
MATRIX:		[3,6,9,16,22]
			[10,13,14,17,24]
			[18,21,23,26,30]
			
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Starting top right
        row, column = 0, len(matrix[0])-1
        
        while row < len(matrix) and column > -1:
            #print(matrix[row][column])
            
            if matrix[row][column] == target:
                return True
            
            # If the value we're checking is less than the target, that means it cannot
            # be on this row and must be on another underneath. This is because any values
            # left of the value being checked are sorted to be less than it, similar with any values
            # underneath the value being check are sorted to be more than it.
            elif matrix[row][column] < target:
                row += 1
                
            # If the value we're checking is greater than the target, we must move left as only smaller
            # values are left of the one we're checking
            else:
                column -= 1
                
        # If the while loop is finished without finding a match, then it does not exist.
        return False