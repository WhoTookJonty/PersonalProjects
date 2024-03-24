from typing import Optional

"""
Note: cannot test solution in development environment, the treeNode class doesn't seem to work here. 


Thoughts:
    Solve this recursively. Have a variable keep track of the greatest depth so far. 
    Have another variable keep track of the current depth so far. Compare this with the greatest depth. 

    To recursively solve it, I need to traverse down every branch of this here tree, until I find a leaf. 
    Once I find a leaf, I can compare whether the current depth is greater than or less than the greatest depth. 
    Perhaps if I minus the current depth each time I traverse backwards, and increment each time I traverse 
    downwards, that would solve my issue. it would. 
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int) -> int:
        ""





