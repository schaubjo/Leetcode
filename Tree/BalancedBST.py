# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    def dfs(root):
        if not root:
            return [True, 0]

        left = dfs(root.left)
        right = dfs(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1] < 2)
        return [balanced, 1 + max(left[1], right[1])]
