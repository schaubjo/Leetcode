# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree(p, q):
    if (not p and q) or (p and not q) or ((p and q) and (p.val != q.val)):
        return False
    
    if not p and not q:
        return True

    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)