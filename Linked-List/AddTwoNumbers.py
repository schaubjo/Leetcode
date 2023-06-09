# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def AddTwoNumbers(l1, l2):
    dummy = ListNode()
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        # new digit
        val = v1 + v2 + carry

        carry = 1 if val > 9 else 0
        val %= 10
        cur.next = ListNode(val)

        # update pointer
        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

n4.next = n5
n5.next = n6

sum = AddTwoNumbers(n1, n4)
while sum:
    print(sum.val)
    sum = sum.next
