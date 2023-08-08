from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    level_to_val = defaultdict(list) # level -> value
    def dfs(root, level):
        if not root:
            return
        level_to_val[level].append(root.val)
        if root.left:
            dfs(root.left, level + 1)
        if root.right:
            dfs(root.right, level + 1)

    dfs(root, 0)
    res = [k for k in level_to_val.values()]
    return res


seven = TreeNode(7)
fifteen = TreeNode(15)
twenty = TreeNode(20, fifteen, seven)
nine = TreeNode(9)
three = TreeNode(3, nine, twenty)
levelOrder(three)





    