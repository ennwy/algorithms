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

        # 1 -> 2 -> 3 -> 4 -> null
        # curr = 1, slow = 3, fast = null

        # second = 4 -> null
        # slow = 1 -> 2 -> 3 -> null

        node = second # 4 -> null
        prev = None # null
        while node:
            nxt = node.next # 
            node.next = prev
            prev = node
            node = nxt

        list1 = head
        list2 = prev

        # list1: 1 → 2 → 3 → null
        # list2: 5 → 4 → null

        while list2:
            nxt1 = list1.next # 2 -> 3 -> null
            nxt2 = list2.next # 4 -> null

            list1.next = list2 # 1 -> 5 -> 2 -> 3 -> nul
            list2.next = nxt1 # 5 -> 2 -> 3 -> nul

            list1 = nxt1
            list2 = nxt2

        # 1 -> 2 -> 3 -> 4 -> null
        # curr = 1, slow = 1, fast = 1

        # 1 -> 2 -> 3 -> 4 -> null
        # curr = 1, slow = 2, fast = 3



        # 
        




        