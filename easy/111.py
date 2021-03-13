class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if self.isLeaf(node):
                return level
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return 0
            
    def isLeaf(self, root):
        return not root.left and not root.right
