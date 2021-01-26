import collections
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check length
        if len(word1) != len(word2):
            return False
        
		# Create Dictionaries
        d1 = {}
        d2 = {}
        for i in word1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] = d1[i]+1
        
        for i in word2:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] = d2[i]+1
        
        # Check Keys
        if set(d1.keys()) != set(d2.keys()):
            return False
        
        vals1 = d1.values()
        vals2 = d2.values()
        
        # Check Values
        return(collections.Counter(vals1) ==  collections.Counter(vals2))