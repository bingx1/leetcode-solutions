class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        queue = collections.deque()
        queue.append((root, 0))
        while queue:
            node, curr_sum = queue.popleft()
            curr_sum += node.val
            if curr_sum  == targetSum and self.isLeaf(node):
                return True
            if node.left:
                queue.append((node.left, curr_sum))
            if node.right:
                queue.append((node.right, curr_sum))
        return False

    def isLeaf(self, root):
        return not root.left and not root.right
