'''
Problem Name: Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

EXAMPLES:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Parameters turn input into INT, this must be returned back into binary and then count the 1s
        return(bin(n).count("1"))