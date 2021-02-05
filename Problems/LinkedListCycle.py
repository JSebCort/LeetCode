'''
Problem Name: Linked List Cycle

Description:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

EXAMPLES:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

(3) -> (2) -> (0) -> (4)
	^	      |
	|-   <--    <-|
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        # Checks for edgecases if the head is empty or has no following node
        if head is None or head.next is None:
            return False
        
        # Two pointers
        slow = head
        fast = head
        
        # Checks while LinkedList is not finished
        while(slow and fast and fast.next):
            
            # Slow will point to the next node, while fast will point 2 nodes ahead.
            # Eventually, if there's a cycle, the two nodes will meet up and the cycle will be found.
            slow = slow.next
            fast = fast.next.next
            
            # Cycle found if both pointers are the same
            if slow == fast:
                return True
        # No cycle if one of the pointers is None, since it would have finished iterating the LinkedList
        return False
