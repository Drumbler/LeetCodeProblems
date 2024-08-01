from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


def printList(head: Optional[ListNode]):
    tmp = head
    while tmp:
        print(tmp.val)
        tmp = tmp.next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]):
        res = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return res


s = Solution()
delete = s.deleteDuplicates(lst2link([1, 1, 1, 1, 2, 3, 4]))
printList(delete)
