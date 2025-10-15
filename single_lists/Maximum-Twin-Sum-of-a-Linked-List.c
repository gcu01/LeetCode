/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

void print_list(struct ListNode *head){
    printf("\n List: ");
    while(head) {
        printf(" %d ", head->val);
        head = head->next;
    }
}

 struct ListNode* inverse_me(struct ListNode *head) {
    struct ListNode *new_head=head, *prev=NULL, *curr=head, *next=head;

    next = next->next;
    while(next) {
        curr->next = prev;
        prev = curr;
        curr = next;//printf("\n curr=%d", curr->val);
        next = next->next;        
    }
    curr->next = prev;
    new_head = curr;
    //print_list(new_head);
    return new_head;
    
 }
int pairSum(struct ListNode* head) {

    if (head==NULL ) return 0;

    struct ListNode *slow=head, *fast=head, *prev=NULL, *half_head=NULL;
    int max=0;

    while(fast && fast->next) {
        prev = slow;
        slow = slow->next;
        fast = fast->next->next;
    }
    
    //printf("\n prev=%d   slow=%d", prev->val, slow->val);
    prev->next = NULL;
    half_head =inverse_me(slow);
    //print_list(head);
    //print_list(half_head);

    while(half_head) {
        if (max < (head->val + half_head->val)) {
            max = head->val + half_head->val;
            //printf("\n max=%d", max);
        }
        head = head->next;
        half_head = half_head->next;
    }

    return max;
}