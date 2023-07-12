'''
Problem Name: Top K Frequent Elements

Description:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
------------------------------------
EXAMPLES:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: Returning the 2 (k) most frequent elements: 1 appears 3 times, 2 appears two times.

Input: nums = [1], k = 1
Output: [1]
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create a list of lists where the number of lists is the length of nums.
        #Each list corresponds to the number of times an integer appears.
        #Ex) At index 4, it means the number stored appeared 4 times. At index 6, it appeared 6 times.
        ans = [[] for i in range(len(nums)+1)]

        #Create a hashmap that pertains to the number of times a given integer appears in nums.
        count = {}

        #Count the number of times an integer appears in nums and store inside count.
        #Ex) nums: [1,1,1,2,2,3]
        #    count: {1: 3, 2: 2, 3: 1}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        #Store the number of times any given number appeared in nums.
        #   ans: [[], [3], [2], [1], [], [], []]
        for n, c in count.items():
            ans[c].append(n)

        #Create a list to return the answer.
        res = []

        #As the numbers are stored in ascending order of number of occurances inside nums,
        #we iterate through ans backwards and append the numbers into res.
        #Ex) ans: [[], [3], [2], [1], [], [], []] ; k = 2
        for i in range(len(ans)-1,0,-1):

            #First run through, we reach [1] and append to res. 
            #Second run through, we reach [2], append to res, and reach out desired K values.
            for j in ans[i]:
                res.append(j)

                #If the length of our res list (our answer) matches the number of K elements desired, return res.
                if len(res) == k:
                    return res