# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        slow, fast = head, head # 

        while fast and fast.next:
            slow = slow.next # 1
            fast = fast.next.next # null

        cur = slow # 1 -> 2 -> 3 -> null
        prev = None

        while cur:
            nextNode = cur.next # null
            cur.next = prev # 3 -> 2 -> 1
            prev = cur # 3 -> 2 -> 1
            cur = nextNode # null

        start, mid = head, prev
        while mid:
            if start.val != mid.val:
                return False

            start = start.next
            mid = mid.next

        return True

