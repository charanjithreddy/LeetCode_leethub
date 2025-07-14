/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int getDecimalValue(struct ListNode* head) {
    int res=0;
    int n=0;
    struct ListNode *temp=head;
    while(temp!=NULL){
        n++;
        temp=temp->next;
    }
    temp=head;
    while(temp!=NULL){
        res+=(temp->val)*pow(2,n-1);
        n--;
        temp=temp->next;
    }
    return res;

}