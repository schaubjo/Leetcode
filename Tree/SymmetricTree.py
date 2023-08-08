# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSymmetric(root):
    def isSameTree(p, q):
        if (not p and q) or (p and not q) or ((p and q) and (p.val != q.val)):
            return False
        
        if not p and not q:
            return True
        
        return isSameTree(p.left, q.right) and isSameTree(p.right, q.left)

    if (not root.left and root.right) or (root.left and not root.right):
        return False

    if not root:
        return True

    return isSameTree(root.left, root.right)