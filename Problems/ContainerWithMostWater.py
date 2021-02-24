'''
Problem Name: Container With Most Water
Description:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

EXAMPLES:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7] (Image found on leetcode website). In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [4,3,2,1,4]
Output: 16
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Two variables that hold the start/end indices of the sliding window
        i, j = 0, len(height)-1
        ans = 0
        
        # While there is a window
        while i<j:
            # Checks to see which height of the start/end is higher, calculates the area,
            # and slides the window by 1 index
            if height[i] <= height[j]:
                hold_val = height[i]*(j-i)
                i += 1
            else:
                hold_val = height[j]*(j-i)
                j -= 1
            
            # If the new calculated area/water contained is greater than ans, store it.
            if hold_val > ans:
                ans = hold_val
                
        return ans
        