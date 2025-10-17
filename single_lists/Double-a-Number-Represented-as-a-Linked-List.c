/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

 void print_me(struct ListNode *head) {
    printf("\n List:");
    while (head){
        printf(" %d ", head->val);
        head = head->next;
    }
 }

 struct ListNode* inverse_me(struct ListNode* head) {
    struct ListNode *prev = NULL, *next = head, *curr = head, *new_head = head;

    next = curr->next;
    while (next) {
        curr->next = prev;
        prev = curr;
        curr = next;
        next = next->next;
    }
    curr->next = prev;
    new_head = curr;
    //printf("\n %d %d", 15/10, 15%10);
//print_me(new_head);
    return new_head;
 }
struct ListNode* doubleIt(struct ListNode* head) {
    
    if(head==NULL) return head;
    struct ListNode *inverse_head=NULL, *new_head=NULL;
    int remainder = 0, sum=0;
    inverse_head = inverse_me(head);
    new_head = inverse_head;

    sum = 2 * inverse_head->val;
    remainder = sum/10;
    sum = sum % 10;
    inverse_head->val = sum;
    if (inverse_head->next == NULL && remainder != 0) {
        inverse_head->next = (struct ListNode*) malloc(sizeof(struct ListNode));
        inverse_head = inverse_head->next;
        inverse_head->val = remainder;
        inverse_head->next = NULL;
    }
    inverse_head = inverse_head->next;

    while (inverse_head) {
        sum = 2 * inverse_head->val + remainder;
        remainder = sum/10;
        sum = sum % 10;
        inverse_head->val = sum;
        sum = 0;
        if (inverse_head->next == NULL && remainder != 0) {
            inverse_head->next = (struct ListNode*) malloc(sizeof(struct ListNode));
            inverse_head = inverse_head->next;
            inverse_head->val = remainder;
            inverse_head->next = NULL;
        }
        inverse_head = inverse_head->next;
    }

return inverse_me(new_head);
}