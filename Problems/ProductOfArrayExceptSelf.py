'''
Problem Name: Product of Array Except Self

Description:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

------------------------------------
EXAMPLES:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Explanation: [2*3*4 = 24; 1*3*4 = 12; 1*2*4 = 8; 1*2*3 = 6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Create an array to hold the product values.
        ans = [1]* len(nums)

        #Variables for the pre and postfix values
        #Prefix = The resulting product between the values to the left of the index.
        #Postfix = The resulting product between the values to the right of the index.
        #Ex) nums = [1,2,3,4] ; The prefix of [2] is [1] as it's the only value left of [2] and the postfix of [2] is [12] as it's (3*4)
        #                       The prefix of [4] is [6] (1*2*3) and the postfix is empty as there's no values to the right of [4]
        pre, post = 1, 1

        #Iterate through the numbers. This lets us calculate the prefix values of every number inside nums.
        #Ex) nums = [1,2,3,4]
        #    ans  = [1,1,2,6] (prefix values)
        for i in range(len(nums)):
            
            #Store the prefix into the answer array
            ans[i] = pre
            #The prefix now becomes the current value * the previous prefix
            pre *= nums[i]
        

        #Iterate through the numbers in reverse order. This lets us calculate the postfix values of every number inside nums.
        #Ex) nums = [1,2,3,4]
        #    ans  = [24, 12, 4, 1] (postfix values)
        for i in range(len(nums)-1, -1, -1):

            #By multiplying the postfix values to the already existing prefix values, we achieve our goal of
            #the product of every element in the list except the selected one.
            ans[i] *= post
            post *= nums[i]

        #Ex) Result: ans = [24,12,8,6]
        return ans