class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head, left, right):
    curr = head
    prev = ListNode(0, curr)
    begin1 = head
    begin2 = head
    for i in range(left):
        if i == left - 1:
            begin1 = prev
        curr = curr.next
        prev = prev.next
    begin2 = prev

    for i in range(right - left):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    end1 = prev
    end2 = curr
    begin1.next = end1
    begin2.next = end2

    return head if left > 1 else end1
