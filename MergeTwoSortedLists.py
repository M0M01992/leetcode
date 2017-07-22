# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(l1 == None):
            return l2;
        if(l2 == None):
            return l1;
        if(l1 == None and l2 == None):
            return None;
        
        Head = ListNode(0)
        ans = ListNode(0);
        Head = ans;
        
        while(l1 and l2):
            if(l1.val > l2.val):
                ans.val = l2.val;
                l2 = l2.next;
                ans.next = ListNode(0);
                ans = ans.next;
            else:
                ans.val = l1.val;
                ans.next = ListNode(0);
                l1 = l1.next;
                ans = ans.next;
                
        while(l1):
            ans.val = l1.val;
            l1 = l1.next;
            if(l1 == None):
                break;
            ans.next = ListNode(0)
            ans = ans.next;
        while(l2):
            ans.val = l2.val;
            l2 = l2.next;
            if(l2 == None):
                break;
            ans.next = ListNode(0);
            ans = ans.next;
        
        return Head;
