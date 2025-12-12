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
                if(list1.val<list2.val):
                    temp1=list1.next;
                    temp2=list2;
                    temp=list1;
                    while(temp1!=None and temp2!=None):
                        if(temp1.val<temp2.val):
                            temp.next=temp1;
                            temp1=temp1.next;
                        else:
                            temp.next=temp2;
                            temp2=temp2.next;
                        temp=temp.next;
                    if(temp1!=None):
                        temp.next=temp1;
                    if(temp2!=None):
                        temp.next=temp2;
                    return list1;
                else:
                    temp2=list2.next;
                    temp1=list1;
                    temp=list2;
                    while(temp1!=None and temp2!=None):
                        if(temp1.val<temp2.val):
                            temp.next=temp1;
                            temp1=temp1.next;
                        else:
                            temp.next=temp2;
                            temp2=temp2.next;
                        temp=temp.next;
                    if(temp1!=None):
                        temp.next=temp1;
                    if(temp2!=None):
                        temp.next=temp2;
                    return list2;
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
        