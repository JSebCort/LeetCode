'''
Problem Name: 3Sum

Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

------------------------------------
EXAMPLES:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, a in enumerate(nums):            
            if  i > 0 and nums[i] == nums[i-1]:
                continue

            lPoint, rPoint = i+1, len(nums)-1

            while lPoint < rPoint:
                threeSum = nums[i] + nums[lPoint] + nums[rPoint]
                if threeSum < 0:
                    lPoint += 1
                elif threeSum > 0:
                    rPoint -= 1
                else:
                    ans.append([nums[i],nums[lPoint],nums[rPoint]])
                    lPoint += 1
                    while nums[lPoint] == nums[lPoint-1] and lPoint < rPoint:
                        lPoint +=1

        return ans