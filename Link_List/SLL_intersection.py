# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None


        t1 = headA
        t2 = headB

        while(True):
            if t1 == t2:
                return t1

            if t1.next == None:
                t1End = t1

            if t2.next == None:
                t2End = t2

            if t1End != None and t2End != None and t1End != t2End:
                return None

            t1 = t1.next
            t2 = t2.next

            if t1 == None:
                t1 = headB

            if t2 == None:
                t2 = headA
