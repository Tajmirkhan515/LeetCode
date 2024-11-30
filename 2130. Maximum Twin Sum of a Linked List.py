
#2130. Maximum Twin Sum of a Linked List

#In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

#For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
#The twin sum is defined as the sum of a node and its twin.

#Given the head of a linked list with even length, return the maximum twin sum of the linked list.




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        

        max_twin_sum = 0
        first, second = head, prev  
        while second:
            twin_sum = first.val + second.val
            max_twin_sum = max(max_twin_sum, twin_sum)
            first = first.next
            second = second.next
        
        return max_twin_sum
        
