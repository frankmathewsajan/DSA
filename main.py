# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        TheSum = ListNode()  
        current = TheSum
        carry = 0

        while l1 or l2 or carry:
            # THE FILLING ZERO TACTIC, LOL
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            # THE MATHS
            total = a + b + carry
            carry = total // 10

            # THE NODE
            current.next = ListNode(total % 10)
            current = current.next

            # MOVING THE POINTERS
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return TheSum.next

"""
Filling ZERO tactic, lol.

We consider that the l1 l2 are equal in length, 
by adding a zero to the end of the shorter list

till list1 and list2 are not empty and carry is not zero
    we add the values of list1 and list2 and carry
    we divide the sum by 10 to get the carry
    we create a new node with the remainder of the sum
    we move the current pointer to the next node
    we move the list1 and list2 pointers to the next node
we return the sum
"""



        