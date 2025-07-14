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
    while(head!=NULL){
        res+=(head->val)*pow(2,n-1);
        n--;
        head=head->next;
    }
    return res;
}