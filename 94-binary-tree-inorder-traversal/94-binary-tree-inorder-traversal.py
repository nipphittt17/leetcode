# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.output = []
        def inorder(root):
            if root is None: return 

            if root.left is not None:
                inorder(root.left)
            self.output.append(root.val)
            if root.right is not None:
                inorder(root.right)
        inorder(root)
        
        return self.output
        

            

        