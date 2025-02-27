# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        if root is None:
            return []
        lefttt=self.inorderTraversal(root.left)
        roottt= [root.val]
        righttt=self.inorderTraversal(root.right)
        return lefttt+roottt+righttt
    

    
        