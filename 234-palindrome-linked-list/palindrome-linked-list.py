# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        prev = None

        while fast and fast.next:
            fast = fast.next.next

            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        if fast:
            slow = slow.next

        left, right = prev, slow
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        
        
    # def isPalindrome(self, head: Optional[ListNode]) -> bool:
    #     nums = []

    #     node = head
    #     while node:
    #         nums.append(node.val)
    #         node = node.next
        
    #     i, j = 0, len(nums) - 1
    #     while i < j:
    #         if nums[i] != nums[j]:
    #             return False

    #         i += 1
    #         j -= 1
            
    #     return True