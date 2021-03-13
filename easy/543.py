class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        output = [1]
        self.depth(root, output)
        return output[-1] - 1
    
    def depth(self, root, output):
        if not root:
            return 0
        L = self.depth(root.left, output)
        R = self.depth(root.right, output)
        output[-1] = max(output[-1], L + R + 1)
        return max(L, R) + 1
