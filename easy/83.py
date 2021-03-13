class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        if not head:
            return None
        while current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
