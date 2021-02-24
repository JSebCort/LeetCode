'''
Problem Name: Search Insert Position
Description:
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

EXAMPLES:

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 7
Output: 4

Input: nums = [1,3,5,6], target = 0
Output: 0
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Iterate through list
        for i in nums:
            
            # If the number being looked at matches the target or is bigger than the target,
            # return the index of the value. This is because:
            # 1) The value is the target, so that is the corresponding index
            # 2) The value is larger than the target but every value before, as the list is sorted,
            #    is smaller than the target. So the target must belong at that index to fit in with the sorting.
            if i >= target:
                return nums.index(i)
            
        # If none of the values are smaller than the target, then the target must belong
        # at the very end of the list, thus being the length of nums.
        return len(nums)