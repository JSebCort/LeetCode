'''
Problem Name: Encode and Decode Strings
Description:
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

------------------------------------
EXAMPLES:
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
'''
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encoded = ""

        for c in strs:
            #Encode the list by adding the length of the string & a '#' symbol.
            encoded += str(len(c)) + "#" + c

        #Ex)   list: ["lint","code","love","you"]
        #   encoded: 4#lint4#code4#love3#you
        return encoded
    
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        #List to hold the decoded strings.
        decoded = []

        #Pointer to hold the start of a new decoded string within the encoded string.
        start = 0

        #While loop that continues until the end of the encoded string.
        while start < len(str):
            #Create a pointer to indicate the end of a encoded string
            end = start
            #Until we find a hashtag symbol, continue searching
            while str[end] != "#":
                end += 1
            #Now that we found a hashtag, we can use the start pointer to store the length of the string, as that's how we encoded it.
            length = int(str[start:end])
            print(length)

            #Given the length of the string, we take a slice of the encoded string, from end+1 until end+1+length.
            #We then append the decoded string to our list.
            decoded.append(str[end + 1 : end + 1 + length])

            #Move the start pointer to after the newly decoded string.
            start = end + 1 + length

        return decoded

test = Solution().encode(["lint","code","love","you"])
test2 = Solution().decode("4#lint4#code4#love3#you")
print(test2)