#------------Only 25% beat-------------#

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
        str1 = "";
        str2 = "";
        nl1 = l1;
        nl2 = l2;
        while(nl1.next != None):
            str1+=str(nl1.val);
            nl1 = nl1.next;
        str1+=str(nl1.val);
        str1r="".join(reversed(str1));
        
        while(nl2.next != None):
            str2+=str(nl2.val);
            nl2 = nl2.next;
        str2+=str(nl2.val);
        str2r="".join(reversed(str2));
        
        temp = int(str1r) + int(str2r);
        strsum = list("".join(reversed(str(temp))));

        
        Head = ListNode(int(strsum[0]));
        if(len(strsum)==1):
            return Head;
        
        Head.next = ListNode(None);
        Node = Head;
        for i in range(len(strsum)):
            Node.val = int(strsum[i]);
            if(i != len(strsum)-1):
                Node.next = ListNode(None);
         
            Node = Node.next
  
        return Head;
