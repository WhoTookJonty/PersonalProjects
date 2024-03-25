from typing import Optional

"""
Its commented out cause I cant find the libraries for TreeNode that LeetCode is using. 

Notes:
    recursively iterate through the nodes until the root.left is null. 
    then recursively iterate until root.right is null. 
    Each time this occurs you have reached the leaf node. 
    Therefore, 

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return
        
        if root.left:
            self.invertTree(root.left)

        if root.right:
            self.invertTree(root.right)
        
        temp = root.right
        root.right = root.left
        root.left = temp
            
        return root