# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        def merge(list1,list2):
            if(list1==None):
                return list2;
            elif(list2==None):
                return list1;
            else:
                head=None;
                if(list1.val<list2.val):
                    head=list1;
                    list1=list1.next;
                else:
                    head=list2;
                    list2=list2.next;
                temp=head;
                while(list1!=None and list2!=None):
                    if(list1.val<list2.val):
                        temp.next=list1;
                        list1=list1.next;
                    else:
                        temp.next=list2;
                        list2=list2.next;
                    temp=temp.next;
                if(list1!=None):
                    temp.next=list1;
                if(list2!=None):
                    temp.next=list2;
                return head;
        if(len(lists)==0):
            return None;
        while(len(lists)>1):
            temp=[];
            for i in range(0,len(lists),2):
                if((i+1)==len(lists)):
                    temp.append(merge(lists[i],None));
                else:
                    temp.append(merge(lists[i],lists[i+1]));
            lists=temp;
        return lists[0];
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """