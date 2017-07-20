# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        absum =0;
        i=0;
      
        
        while(l1 and l2):
            absum += l1.val * (10**i) + l2.val * (10**i);
            i=i+1;
            l1 = l1.next;
            l2 = l2.next;
        if(l1!=None):
            while(l1):
                absum += l1.val * (10**i);
                l1 = l1.next;
                i=i+1;
        elif(l2!=None):
            while(l2):
                absum += l2.val * (10**i);
                l2 = l2.next;
                i=i+1; 
                
        
        Head = ListNode(absum%10);
        if(absum < 10):
            return Head;
        
        Head.next = ListNode(0);
        Node = Head.next;
        absum = absum/10;
        while (absum > 0):
            Node.val = absum%10;
            if(absum > 9):
                Node.next = ListNode(0);
            absum = absum/10;
            Node = Node.next;

  
        return Head;
