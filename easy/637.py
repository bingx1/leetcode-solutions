class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = collections.deque()
        output = []
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
            if len(output) < level + 1:
                output.append([node.val])
            else:
                output[-1].append(node.val)
        return [sum(x)/len(x) for x in output]
