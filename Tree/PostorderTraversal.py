class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    def traversal(root):
        if root.left:
            traversal(root.left)
        if root.right:
            traversal(root.right)
        res.append(root.val)

    res = []
    if not root:
        return res

    traversal(root)

    return res
