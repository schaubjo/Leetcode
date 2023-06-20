class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):
    curr, next = root, root.left if root else None

    while curr and next:
        curr.left.next = curr.right
        if curr.next:
            curr.right.next = curr.next.left

        curr = curr.next
        if not curr:
            curr = next
            next = curr.left

    return root
