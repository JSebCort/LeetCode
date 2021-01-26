# Problem Name: Check If All 1's Are at Least Length K Places Away
# Description: Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.

'''
EXAMPLE
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
'''

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        count, counter = [], 0
        
        # Work through list of numbers
        for i in nums:
            # If num is 1, start counter
            if i==1:
                count.append(counter)
                counter=0
            # If num is 0, add to counter
            else:
                counter = counter+1
                
        if 0 in count:        
            count.remove(0)
        
        for i in count:
            if i < k:
                return False
            
        return True
