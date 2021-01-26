class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        count, counter = [], 0
        
        # Work through list of numbers
        for i in nums:
            # If num is 1, start counter
            if i==1:
                count.append(counter)
                counter=0
            # If num is 0, add to counter
            else:
                counter = counter+1
                
        if 0 in count:        
            count.remove(0)
        
        for i in count:
            if i < k:
                return False
            
        return True