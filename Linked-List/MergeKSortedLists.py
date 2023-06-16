class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# merge 2 sorted lists


def mergeTwo(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2
    return dummy.next


def mergeKLists(lists):
    if not lists or len(lists) == 0:
        return None
    # merge pairs of linked lists until only 1 remaining list
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeTwo(l1, l2))
        lists = mergedLists

    return lists[0]


a3 = ListNode(5)
a2 = ListNode(4, a3)
a1 = ListNode(1, a2)

b3 = ListNode(4)
b2 = ListNode(3, b3)
b1 = ListNode(1, b2)

c2 = ListNode(6)
c1 = ListNode(2, c2)

lists = [a1, b1, c1]

res = mergeKLists(lists)
print("pass")
while res:
    print(res.val)
    res = res.next
