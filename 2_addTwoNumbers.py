# You are given two non-empty linked lists representing 
# two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. Add the two numbers and return the 
# sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 
# 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

#https://leetcode.com/problems/add-two-numbers/

l1 = [2,4,3]
l2 = [5,6,4]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(l1: ListNode,l2:ListNode):
    l3 = ListNode(0)
    l3_tail = l3
    carry = 0

    while(l1 or l2 or carry):
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        carry,out = divmod(val1+val2+carry,10)
        l3_tail.next = ListNode(out)
        l3_tail = l3_tail.next

        l1 = (l1.next if l1 else None)
        l2 = (l2.next if l2 else None)
    return l3.next

solution(l1,l2)
