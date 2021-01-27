'''
Problem Name: Concatenation of Consecutive Binary Numbers
Description: Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

Example:
Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
'''
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # Create variable to hold the binary string
        binary = ""
        
        # For every number from 1 to n
        for i in range(1,n+1):
            
            # Convert number to binary, and append it to the tail of the 'binary' string
            binary+=str(bin(i).replace("0b",""))
        
        # Return the conversion of the 'binary' string back to decimal
        return(int(binary,2)%(10**9+7))