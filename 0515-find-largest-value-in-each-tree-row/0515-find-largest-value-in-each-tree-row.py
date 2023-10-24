# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []

        q = collections.deque([root])
        while q:
            temp = float("-inf")
            for i in range(len(q)):
                node = q.popleft()
                temp = max(temp, node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            res.append(temp)
        
        return res