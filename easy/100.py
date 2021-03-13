class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and not q or q and not p:
            return False
        if not p and not q:
            return True
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
