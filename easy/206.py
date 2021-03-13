class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        node = head
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev
