'''
Problem Name: Broken Calculator
Description:
On a broken calculator that has a number showing on its display, we can perform two operations:

    Double: Multiply the number on the display by 2, or;
    Decrement: Subtract 1 from the number on the display.

Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.

EXAMPLES:
Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.

Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
'''
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        # We will go in reverse: Changing Y into X.
        # This lets us do division of Y by 2 to quickly get to X.
        while X < Y:
        
            # Counting the number of operations done
            ans += 1
            
            # If Y is even, we can divide by 2
            if Y % 2 == 0:
                Y /= 2
                
            # Else, we add 1 so that we make it even.
            else:
                Y += 1
        
        # Since dividing Y by 2 can get us below X, we simply take the difference of X and Y
        # to account for the extra additions of 1 needed to match the two variables up.
        return int(X-Y) + ans