class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root: return 0
        level, stack = 0, [root] 

        while stack:

            level+= 1

            for x in range(len(stack)):

                node = stack.pop(0)
                if not node.left and not node.right: return level

                if node.left : stack.append(node. left)
                if node.right: stack.append(node.right)