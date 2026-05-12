# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []

        node = head
        while node:
            nums.append(node.val)
            node = node.next
        
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] != nums[j]:
                return False

            i += 1
            j -= 1
            
        return True