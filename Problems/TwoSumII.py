'''
Problem Name: Two Sum II - Input Array Is Sorted

Description:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

------------------------------------
EXAMPLES:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Create a left (the first value in numbers) and right pointer (the last value in numbers).
        lPoint, rPoint = 0, len(numbers)-1

        while True:
            sum = numbers[lPoint] + numbers[rPoint]

            #If the sum is less than the target, we increase the left pointer as, since the list is ordered, the next sum will be larger.
            if sum < target:
                lPoint += 1
            #If the sum is more than the target, we decrease the right pointer to decrease the overall sum.
            elif sum > target:
                rPoint -= 1
            #Return the pointers' values +1, since the problem has the list 1-based.
            else:
                return [lPoint+1,rPoint+1]