from typing import Optional
from openai import OpenAI


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


def print_list(head: Optional[ListNode]):
    tmp = head
    while tmp:
        print(tmp.val)
        tmp = tmp.next


class LinkedListCycle(object):
    def hasCycle(self, head) -> bool:
        visited = set()
        curr = head
        count = 0
        while curr is not None:

            if curr in visited:
                return True

            count += 1
            visited.add(curr)
            curr = curr.next
        return False


s = LinkedListCycle()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)

head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head.next

print(s.hasCycle(head))
