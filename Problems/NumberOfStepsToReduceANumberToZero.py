'''
Problem Name: Number of Steps to Reduce a Number to Zero
Description: Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

EXAMPLE:
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
'''
class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        
        # While the number is not 0
        while num > 0:
            
            # If it's even, it can be reduced by half
            if num % 2 == 0:
                num /= 2
                
            # Else, simply subtract by 1
            else:
                num -= 1
            
            # Count the number of times inside the while loop
            count += 1
            
        return count