'''
Problem Name: Longest Consecutive Sequence
Description:
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
------------------------------------
EXAMPLES:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Create a set to handle the *consecutive* portion of the problem.
        num = set(nums)

        #Answer variable.
        ans = 0

        #Iterate through the numbers.
        for i in nums:
            #Check if (i-1) exists. If false, it means we're at the start of a new sequence.
            if (i-1) not in nums:
                #Temporary sequence length variable.
                temp = 0
                #While there is a consecutive sequence (i, i+1, i+2, etc.), add to the length of the sequence (temp += 1)
                while (i+temp) in num:
                    temp += 1
                #Store the larger values between the temp value and the answer value.
                ans = max(temp,ans)
        
        return ans