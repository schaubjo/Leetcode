import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    q = collections.deque()

    q.append(root)
    res = []
    while q:
        level = []
        for i in range(len(q)):
            new_element = q.popleft()
            if new_element:
                level.append(new_element.val)
                q.append(new_element.left)
                q.append(new_element.right)
        if len(level) > 0:
            res.append(level)
    
    return res

    
        

            
            




seven = TreeNode(7)
fifteen = TreeNode(15)
twenty = TreeNode(20, fifteen, seven)
nine = TreeNode(9)
three = TreeNode(3, nine, twenty)
print(levelOrder(three))





    