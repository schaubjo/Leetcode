# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode()
    dummy.next = head
    fast = dummy
    slow = dummy

    for i in range(n):
        fast = fast.next

    while fast:
        if not fast.next:
            slow.next = slow.next.next
        fast = fast.next
        slow = slow.next

    return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

res = removeNthFromEnd(n1, 1)
while res:
    print(res.val)
    res = res.next
