'''
Problem Name: Merge Two Sorted Lists

Description: Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

EXAMPLE: 
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Create a new Node and a reference to the node
        merged = ListNode()
        ans = ListNode(0)
        merged = ans
        
        while(True):
            # If both lists are empty, break out of loop
            if l1 is None and l2 is None:
                break
                
            # If l1 is empty, then add the remaining nodes of l2 to merged
            elif l1 is None:
                merged.next = l2
                break
                
            # If l2 is empty, then add the remaining nodes of l1 to merged
            elif l2 is None:
                merged.next = l1
                break
                
            # Check the values and add the smaller of the two to merged, then move a node over
            else:
                if l1.val <= l2.val:
                    merged.next = ListNode(l1.val,None)
                    merged = merged.next
                    l1 = l1.next
                else:
                    merged.next = ListNode(l2.val,None)
                    merged = merged.next
                    l2 = l2.next
     
        return ans.next