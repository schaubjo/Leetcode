# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head, val):
    dummy = ListNode()
    dummy.next = head
    slow = dummy
    fast = head
    while fast:
        if fast.val == val:
            fast = fast.next
            if not fast:
                slow.next = fast
        else:
            slow.next = fast
            slow = slow.next
            fast = fast.next

    return dummy.next


n6 = ListNode(6)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(6, n3)
n1 = ListNode(2, n2)
n0 = ListNode(1, n1)

res = removeElements(n0, 6)
while res:
    print(res.val)
    res = res.next
