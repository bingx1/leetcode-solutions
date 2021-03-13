class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead = ListNode(-1, head)
        current = newHead
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return newHead.next
