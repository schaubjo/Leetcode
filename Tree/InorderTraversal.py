class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    def traversal(root):
        if root.left:
            traversal(root.left)

        res.append(root.val)

        if root.right:
            traversal(root.right)

    res = []
    if not root:
        return res

    traversal(root)
    return res


root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
print(inorderTraversal(root))
