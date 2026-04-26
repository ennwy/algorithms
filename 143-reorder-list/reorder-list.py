# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        node = second
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        list1 = head
        list2 = prev
        
        while list2:
            nxt1, nxt2 = list1.next, list2.next

            list1.next = list2
            list2.next = nxt1

            list1 = nxt1
            list2 = nxt2
        




        