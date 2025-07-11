/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode *temp=head;
    int l=0;
    while(temp!=NULL){
        temp=temp->next;
        l++;
    }
    temp=head;
    for(int i=0;i<l-n-1;i++){
        temp=temp->next;
    }
    if(l==n){
        head=temp->next;
    }
    else{
        temp->next=temp->next->next;
    }
    return head;
    
}