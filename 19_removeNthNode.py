# Given the head of a linked list, remove the nth node from
# the end of the list and return its head.

# Input: head = [1, 2, 3, 4, 5], n = 2
# Output: [1, 2, 3, 5]

# Input: head = [1], n = 1
# Output: []

# Input: head = [1, 2], n = 1
# Output: [1]

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0

        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next

        if(n == length):
            head = head.next
            return head

        ptr = head
        for i in range(1, length+1):
            # prev node to the to be deleted
            if(i == length - n):
                ptr.next = ptr.next.next
                break
            ptr = ptr.next

        return head

# RECURSIVE
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         def index(node):
#             if not node:
#                 return 0
#             i = index(node.next) + 1
#             if i > n:
#                 node.next.val = node.val
#             return i
#         index(head)
#         return head.next


if __name__ == '__main__':

    node5 = ListNode(5, None)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    linkedList = ListNode(1, None)

    solution = Solution()
    print(solution.removeNthFromEnd(linkedList, 1))
