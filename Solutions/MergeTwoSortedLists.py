class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_LL(self):
        curr = self
        while curr:
            print(curr.val)
            curr = curr.next

    @staticmethod
    def from_list(values):
        head = ListNode()
        curr = head
        for v in values:
            curr.next = ListNode(v)
            curr = curr.next
        return head.next


def merge_two_lists(list1, list2):
    curr = head = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2
    ListNode.print_LL(head)
    return head.next


l1 = ListNode.from_list([1, 2, 4])
l2 = ListNode.from_list([1, 3, 4])

print(merge_two_lists(l1, l2))
