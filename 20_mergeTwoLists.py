# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ptr1 = list1
        ptr2 = list2
        head = ListNode()
        ptr3 = head

        if not ptr1 and not ptr2:
            return None

        while(ptr1 or ptr2):
            if(ptr1 and ptr2):
                if ptr1.val >= ptr2.val:
                    ptr3.val = ptr2.val
                    ptr2 = ptr2.next
                else:
                    ptr3.val = ptr1.val
                    ptr1 = ptr1.next

                if(ptr1 or ptr2):
                    ptr3.next = ListNode()
                    ptr3 = ptr3.next

            elif(ptr1):
                ptr3.val = ptr1.val
                if(ptr1.next):
                    ptr3.next = ListNode()
                    ptr3 = ptr3.next
                ptr1 = ptr1.next
            else:
                ptr3.val = ptr2.val
                if(ptr2.next):
                    ptr3.next = ListNode()
                    ptr3 = ptr3.next
                ptr2 = ptr2.next

        return head

    def mergeTwoLists2(self, l1, l2):
        l3 = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return l3.next

    def mergeTwoLists3(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
