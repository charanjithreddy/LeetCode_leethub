# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if(list1==None):
            if(list2==None):
                return None;
            else:
                return list2;
        elif(list2==None):
            return list1;
        else:
            temp=None;
            if(list1.val<list2.val):
                temp=list1;
                list1=list1.next;
            else:
                temp=list2;
                list2=list2.next;
            head=temp;
            while(list1!=None and list2!=None):
                if(list1.val<list2.val):
                    temp.next=list1;
                    temp=temp.next;
                    list1=list1.next;
                else:
                    temp.next=list2;
                    temp=temp.next;
                    list2=list2.next;
            while(list1):
                temp.next=list1;
                temp=temp.next;
                list1=list1.next;
            while(list2):
                temp.next=list2;
                temp=temp.next;
                list2=list2.next;
            return head;
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """