class Solution:
    def isPalindrome(self, head):
        rev = None
        slow = fast = head
#         Reverse front of the list
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
#         Check fast isn't none - for cases where the linked list is an odd length
        if fast:
            slow = slow.next
#         Compare with second half of list 
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
