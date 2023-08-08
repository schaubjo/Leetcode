from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def zigzagLevelOrder(root):
    q = deque()
    q.append(root)
    zags = 0
    res = []
    while q:
        level = []
        if zags % 2 == 0:
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
        elif zags % 2 == 1:
            for i in range(len(q)):
                node = q.pop()
                if node:
                    level.append(node.val)
                    q.appendleft(node.right)
                    q.appendleft(node.left)
        
        if len(level) > 0:
            res.append(level)
        zags += 1
    
    return res

seven = TreeNode(7)
fifteen = TreeNode(15)
twenty = TreeNode(20, fifteen, seven)
nine = TreeNode(9)
three = TreeNode(3, nine, twenty)
print(zigzagLevelOrder(three))
        
