# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def valid(root, left_bound, right_bound):
        if not root:
            return True
        if not (left_bound < root.val < right_bound):
            return False
        
        return valid(root.left, left_bound, root.val) and valid(root.right, root.val, right_bound)
    
    return valid(root, -float('inf'), float('inf'))