class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root):
    res = []
    if not root:
        return res

    def traverse(root):
        res.append(root.val)
        if root.left:
            traverse(root.left)
        if root.right:
            traverse(root.right)

    traverse(root)
    return res


root = TreeNode(1, None, TreeNode(2, TreeNode(3, None, None), None))
print(preorderTraversal(root))
