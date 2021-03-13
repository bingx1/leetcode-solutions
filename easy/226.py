class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        else:
            return TreeNode(root.val, self.invertTree(root.right), self.invertTree(root.left))
