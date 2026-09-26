# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        queue=deque()
        res=[]
        queue.append(root)
        while len(queue):
            l=len(queue)
            level=[]
            for i in range(l):
                front=queue.popleft()
                level.append(front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            res.append(level)
        res.reverse()
        return res